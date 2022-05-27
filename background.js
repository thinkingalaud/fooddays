var MONTHS = ['January','February','March','April','May','June','July','August','September','October','November','December'];
var WEEKDAYS = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'];
var WEEKDAYS_FULL = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
var WEEKNUM = ['First', 'Second', 'Third', 'Fourth', 'Fifth'];
var DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

var totalElements = 21;

var UNEVENTFULS = [
  ["images/donut.png", "Donut worry - another food day is coming up soon!"],
  ["images/peanut.png", "Don't go nuts - another food day is coming up soon!"],
  ["images/romaine.png", "Romaine calm - another food day is coming up soon!"],
  ["images/kiwi.png", "There's no food day today - it's kiwing me too."],
  ["images/tempura.png", "Don't lose your tempura - another food day is coming up soon!"],
  ["images/matcha.png", "Don't freak out too matcha - another food day is coming up soon!"],
  ["images/dill.png", "There's no food day today - I hope it's not too big of a dill!"]
];

// Downloaded from https://www.iconfinder.com/iconsets/world-flag-icons
var COUNTRIES = {
  "Global": "images/flags/Global.png",
  "Africa": "images/flags/Flag_of_South_Africa.png",
  "Australia": "images/flags/Flag_of_Australia.png",
  "Brazil": "images/flags/Flag_of_Brazil.png",
  "Canada": "images/flags/Flag_of_Canada.png",
  "Finland": "images/flags/Flag_of_Finland.png",
  "Georgia": "images/flags/Flag_of_Georgia.png",
  "Germany": "images/flags/Flag_of_Germany.png",
  "Iceland": "images/flags/Flag_of_Iceland.png",
  "India": "images/flags/Flag_of_India.png",
  "Italy": "images/flags/Flag_of_Italy.png",
  "Japan": "images/flags/Flag_of_Japan.png",
  "Korea": "images/flags/Flag_of_South_Korea.png",
  "Luxembourg": "images/flags/Flag_of_Luxembourg.png",
  "Netherlands": "images/flags/Flag_of_Netherlands.png",
  "New Zealand": "images/flags/Flag_of_New_Zealand.png",
  "Spain": "images/flags/Flag_of_Spain.png",
  "Sweden": "images/flags/Flag_of_Sweden.png",
  "Turkmenistan": "images/flags/Flag_of_Turkmenistan.png",
  "United Kingdom": "images/flags/Flag_of_United_Kingdom.png",
  "United States": "images/flags/Flag_of_United_States.png"
}

// Helper functions used in child pages

function newWeekviewElement(id) {
  return '<div id="weekview' + id + '" class="weekday-bubble"></div>'
}

function newDisplayElement(id) {
  return '<div id="info' + id + '" class="info-display"> <div class="info-title"></div> <div class="info-content"> </div> </div>'
}

function newDots(num) {
  res = '';
  for(var i = 0; i < num; i++) {
    res += '\u2022';
  }
  return res;
}

function addInfo(element) {
  info = document.createElement("div");
  info.className = "info-single";

  day = document.createElement("div");
  day.className = "info-day";
  info.appendChild(day);

  subelement = element.getElementsByClassName("info-content")[0];
  subelement.appendChild(info);

  return [info, day]
}

function createUneventfulSubtext() {
  uneventful = document.createElement("div");
  uneventful.className = "img-subtext-uneventful";
  uneventful.innerHTML = "art by <a target='_blank' href='https://www.instagram.com/subtle_smiles/'>subtle_smiles</a>"
  return uneventful;
}

function createCornerFlag(flagSrc, tooltipText) {
  cornerBox = document.createElement("div");
  cornerBox.className = "corner-box";
  cornerTip = document.createElement("div");
  cornerTip.className = "corner-tip";
  cornerContents = document.createElement("div");
  cornerContents.className = "corner-contents";
  flag = document.createElement("img");
  flag.className = "img-subtext-country";
  flag.src = flagSrc;
  tooltip = document.createElement("span");
  tooltip.className = "tooltiptext";
  tooltip.innerHTML = tooltipText;

  cornerBox.appendChild(cornerTip);
  cornerTip.appendChild(cornerContents);
  cornerContents.appendChild(flag);
  return [cornerBox, tooltip]
}

function getFullDate(day) {
  return day.getFullYear() + "-" + day.getMonth() + "-" + day.getDate();
}

function populateElement(element, result) {
  element.getElementsByClassName("info-title")[0].innerHTML = result['date'];
  if (result['days'].length == 0) {
    infoElements = addInfo(element);
    index = result['raw_date'].getDate() % UNEVENTFULS.length
    infoElements[0].style.backgroundImage = "url(" + UNEVENTFULS[index][0] + ")";
    infoElements[0].appendChild(createUneventfulSubtext());
    infoElements[1].classList.add("info-day-uneventful");
    infoElements[1].innerHTML = UNEVENTFULS[index][1];
  } else {
    for (var j = 0; j < result['days'].length; j++) {
      infoElements = addInfo(element);
      infoElements[0].style.backgroundImage = "url('" + result['imgs'][j] + "')";
      cornerFlag = createCornerFlag(COUNTRIES[result['countries'][j]], result['countries'][j]);
      infoElements[0].appendChild(cornerFlag[0]);
      infoElements[0].appendChild(cornerFlag[1]);
      infoElements[1].innerHTML = "<a target='_blank' href=\"https://www.google.com/search?q=" + encodeURIComponent(result['days'][j]) + "\">" + result['days'][j] + "</a>";
    }
  }
}

// End helper functions


function getSynonyms(date) {
  var res = [];
  res.push(MONTHS[date.getMonth()] + ' ' + date.getDate());
  res.push(WEEKNUM[Math.floor((date.getDate() - 1) / 7)] + ' ' + WEEKDAYS_FULL[date.getDay()] + ' of ' + MONTHS[date.getMonth()]);
  res.push(WEEKNUM[Math.floor((date.getDate() - 1) / 7)] + ' ' + WEEKDAYS_FULL[date.getDay()] + ' in ' + MONTHS[date.getMonth()]);
  if ((date.getDate() + 7) > DAYS_IN_MONTH[date.getMonth()]) {
    res.push('Last ' + WEEKDAYS_FULL[date.getDay()] + ' of ' + MONTHS[date.getMonth()]);
    res.push('Last ' + WEEKDAYS_FULL[date.getDay()] + ' in ' + MONTHS[date.getMonth()]);
  }

  return res;
}

function getInfo(today, callback) {
  data = [];
  for (var i = (-(totalElements/2) >> 0); i < ((totalElements/2) >> 0) + 1; i++) {
    var day = new Date(today.getTime());
    day.setDate(today.getDate() + i);
    var day_strs = getSynonyms(day);
    
    d = {};
    d['date'] = day_strs[0];
    d['raw_date'] = day;
    d['dow'] = day.getDay();
    d['days'] = [];
    d['countries'] = [];
    d['imgs'] = [];

    for (var j = 0; j < day_strs.length; j++) {
      var day_str = day_strs[j];
      if (day_str in cache) {
        days = cache[day_str];
        for (var k = 0; k < days.length; k++) {
          d['days'].push(days[k][0]);
          d['countries'].push(days[k][1]);
          d['imgs'].push(img_cache[[day_str, days[k][0]]]);
        }
      }
    }
    data.push(d);
  }
  callback(data);
}

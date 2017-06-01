var DEFAULT_BACKGROUND_COLOR = '#FFFFFF';
var DEFAULT_FONT_COLOR = '#000000';

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

// Helper functions used in child pages

function newWeekviewElement(id) {
  return '<div id="weekview' + id + '" class="weekday-bubble"></div>'
}

function newDisplayElement(id) {
  return '<div id="info' + id + '" class="info-display"> <div class="info-title"></div> <div class="info-content"> <div class="info-imgs"></div> <div class="info-days"></div> </div> </div>'
}

function newDots(num) {
  res = '';
  for(var i = 0; i < num; i++) {
    res += '\u2022';
  }
  return res;
}

function addInfo(element) {
  img = document.createElement('div');
  img.className = 'info-img';
  subelement = element.getElementsByClassName('info-imgs')[0];
  subelement.appendChild(img);

  day = document.createElement('div');
  day.className = 'info-day';
  subelement = element.getElementsByClassName('info-days')[0];
  subelement.appendChild(day);

  return [img, day]
}

function getFullDate(day) {
  return day.getFullYear() + '-' + day.getMonth() + '-' + day.getDate();
}

function populateElement(element, result) {
  element.getElementsByClassName("info-title")[0].innerHTML = result['date'];
  if (result['days'].length == 0) {
    infoElements = addInfo(element);
    index = result['raw_date'].getDate() % UNEVENTFULS.length
    infoElements[0].style.backgroundImage = "url(" + UNEVENTFULS[index][0] + ")";
    infoElements[0].innerHTML = "<div class='img-subtext'>art by <a target='_blank' href='https://www.instagram.com/subtle_smiles/'>subtle_smiles</a></dev>";
    infoElements[1].classList.add("info-day-uneventful");
    infoElements[1].innerHTML = UNEVENTFULS[index][1];
  } else {
    for (var j = 0; j < result['days'].length; j++) {
      infoElements = addInfo(element);
      infoElements[0].style.backgroundImage = "url('" + result['imgs'][j] + "')";
      infoElements[1].innerHTML = result['days'][j];
    }
  }
}

// End helper functions


function getSynonyms(date) {
  var res = [];
  res.push(MONTHS[date.getMonth()] + ' ' + date.getDate());
  res.push(WEEKNUM[Math.floor((date.getDate() - 1) / 7)] + ' ' + WEEKDAYS_FULL[date.getDay()] + ' of ' + MONTHS[date.getMonth()]);
  if ((date.getDate() + 7) > DAYS_IN_MONTH[date.getMonth()]) {
    res.push('Last ' + WEEKDAYS_FULL[date.getDay()] + ' of ' + MONTHS[date.getMonth()]);
  }

  return res;
}

function getInfo(today, callback) {
  console.log(today);
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
    d['imgs'] = [];

    for (var j = 0; j < day_strs.length; j++) {
      var day_str = day_strs[j];
      console.log(day_str);
      console.log(day_str in cache);
      if (day_str in cache) {
        days = cache[day_str];
        for (var k = 0; k < days.length; k++) {
          console.log([day_str, days[k]]);
          d['days'].push(days[k]);
          d['imgs'].push(img_cache[[day_str, days[k]]]);
        }
      }
    }
    data.push(d);
  }
  callback(data);
}

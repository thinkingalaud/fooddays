var DEFAULT_BACKGROUND_COLOR = '#FFFFFF';

// Google Analytics code
var _gaq = _gaq || [];
_gaq.push(['_setAccount', 'UA-98193595-1']);
_gaq.push(['_trackPageview']);

(function() {
  var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
  ga.src = 'https://ssl.google-analytics.com/ga.js';
  var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
})();

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


function refresh(date, forward) {
  var window = chrome.extension.getBackgroundPage();
  document.currentDate = date;
  window.getInfo(date, function(results) {
    // Moving backwards in time means that we should be inserting new elements from the right to ensure the correct order
    if (!forward) {
      results.reverse();
    }

    for (var i = 0; i < results.length; i++) {
      var result = results[i];
      var full_date = getFullDate(result['raw_date']);
      var element_id = 'info' + full_date;
      var weekview_id = 'weekview' + full_date;
      var found = document.getElementById(element_id);

      if (found) {
        // console.log('Found ' + element_id);
      } else {
        // Add new slides
        console.log('Adding ' + full_date);
        // If we insert at the beginning all slides get shifted to the right but we need to make sure the current slide doesn't change
        if (!forward) {
          $('#weekview')[0].slick.currentSlide += 1;
          $('#info')[0].slick.currentSlide += 1;
        }
        $('#weekview').slick('slickAdd', newWeekviewElement(full_date), !forward);
        $('#info').slick('slickAdd', newDisplayElement(full_date), !forward);

        // Populate all the info
        dots = newDots(result['days'].length);
        document.getElementById(weekview_id).innerHTML = '<span>' + window.WEEKDAYS[result['dow']] + '<br/>' + result['raw_date'].getDate() + '<br/>' + dots + '</span>';
        document.getElementById(element_id).getElementsByClassName("info-title")[0].innerHTML = result['date'];
        if (result['days'].length == 0) {
          infoElements = addInfo(document.getElementById(element_id));
          infoElements[1].innerHTML = "There is nothing happening today!";
        } else {
          for (var j = 0; j < result['days'].length; j++) {
            infoElements = addInfo(document.getElementById(element_id));
            infoElements[0].style.backgroundImage = "url('" + result['imgs'][j] + "')";
            infoElements[1].innerHTML = result['days'][j];
          }
        }
      }
    }
    // TODO: delete elements that are not found in the results to reduce cruft
  });
}

$(document).ready(function() {
  // Set saved color background immediately
  chrome.storage.local.get({"backgroundColor": "", "dateColor": "", "textColor": ""}, function(items) {
    backgroundColor = items.backgroundColor ? items.backgroundColor : DEFAULT_BACKGROUND_COLOR;
    document.body.style.backgroundColor = backgroundColor;
    document.getElementById("backgroundColorPicker").jscolor.fromString(backgroundColor);
  });

  // Set up slider
  var window = chrome.extension.getBackgroundPage();
  $('#weekview').slick({
    variableWidth: true,
    adaptiveHeight: true,
    asNavFor: '#info',
    centerMode: true,
    centerPadding: '60px',
    slidesToShow: 3,
    respondTo: 'slider',
    swipe: false,
    focusOnSelect: true,
    prevArrow: '<svg class="slick-prev slick-arrow"><line class="arrow" x1="100%" y1="0%" x2="0%" y2="50%"/><line class="arrow" x1="0%" y1="50%" x2="100%" y2="100%"/></svg>',
    nextArrow: '<svg class="slick-next slick-arrow"><line class="arrow" x1="0%" y1="0%" x2="100%" y2="50%"/><line class="arrow" x1="100%" y1="50%" x2="0%" y2="100%"/></svg>'
  })
  $('#info').slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: false,
    swipe: false,
    fade: true,
    asNavFor: '#weekview'
  });

  // Initialize actual slides based on today's date
  document.currentDate = new Date();
  document.prevSlide = 0;
  refresh(document.currentDate, true);

  // Reset current date so that when we call goto and start in the middle, currentDate gets set to the correct date
  document.currentDate.setDate(document.currentDate.getDate() - (window.totalElements / 2 >> 0));

  // Initialize to middle of the slider
  $('#info').slick('slickGoTo', (window.totalElements / 2 >> 0));

  // Add event handlers for updating days as people move through the calendar
  $('#weekview').on('beforeChange', function(event, slick, currentSlide, nextSlide) {
    // afterChange doesn't have access to the slide before
    document.prevSlide = Number(currentSlide);
  });
  $('#weekview').on('afterChange', function(event, slick, currentSlide) {
    var diff = currentSlide - document.prevSlide;
    var date = new Date(document.currentDate.getTime());
    date.setDate(document.currentDate.getDate() + diff);
    refresh(date, currentSlide > document.prevSlide);
  });

  // Settings modal
  var settingsModal = document.getElementById('settings');
  var btn = document.getElementById("settings-btn");
  btn.onclick = function() {
    settingsModal.style.display = "block";
  }
  var close = document.getElementsByClassName("close")[0];
  close.onclick = function() {
    settingsModal.style.display = "none";
  }
  // When the user clicks anywhere outside of the modal, close it
  document.onclick = function(event) {
    if (event.target == settingsModal) {
      settingsModal.style.display = "none";
    }
  }

  // Settings modal - background color
  var colorPickers = document.getElementById("settings-color").getElementsByClassName("color-picker-value");
  for (var i = 0; i < colorPickers.length; i++) {
    var picker = colorPickers[i];
    picker.onchange = function(e) {
      color = e.target.value;
      chrome.storage.local.set({"backgroundColor": color}, function() {
        document.body.style.backgroundColor = color;
      });
    }
  }

  // Add Google Analytics tracking for buttons
  $('#weekview').on('click', '.slick-arrow.slick-prev', function() {
    _gaq.push(['_trackEvent', 'prevarrow', 'clicked']);
  });
  $('#weekview').on('click', '.slick-arrow.slick-next', function() {
    _gaq.push(['_trackEvent', 'nextarrow', 'clicked']);
  });
  // Add Google Analytics tracking for dates
  $('#weekview').on('click', 'div.weekday-bubble', function() {
    _gaq.push(['_trackEvent', 'date', 'clicked']);
  })
});


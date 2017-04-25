function mod(n, m) {
  return ((n % m) + m) % m;
}

function refresh(date, nextSlide) {
  var window = chrome.extension.getBackgroundPage();
  window.currentDate = date;
  window.get_info(date, function(results) {
    start = mod(nextSlide - ((window.totalElements / 2) >> 0), window.totalElements);
    console.log(start);
    
    for (var i = 0; i < results.length; i++) {
      result = results[i];
      element_index = mod((i + start), window.totalElements);
      element_id = 'info' + element_index;
      console.log(element_id);
      console.log(result);

      document.getElementById('weekview' + element_index).innerText = window.WEEKDAYS[result['dow']];
      if (result['days'] == null) {
        document.getElementById(element_id).getElementsByClassName("info-title")[0].innerHTML = result['date'];
        document.getElementById(element_id).getElementsByClassName("info-days")[0].innerHTML = "There is nothing happening today!";
      } else {
        // TODO: handle multiple days in result like February 9 or July 4
        document.getElementById(element_id).getElementsByClassName("info-title")[0].innerHTML = result['date'];
        document.getElementById(element_id).getElementsByClassName("info-days")[0].innerHTML = result['days'][0];
        document.getElementById(element_id).getElementsByClassName("info-img")[0].style.backgroundImage = "url('" + result['img'][0] + "')";
      }
    }
  });
}

$(document).ready(function() {
  var window = chrome.extension.getBackgroundPage();
  $('#weekview').slick({
    initialSlide: (window.totalElements / 2 >> 0),
    variableWidth: true,
    adaptiveHeight: true,
    asNavFor: '#info',
    centerMode: true,
    centerPadding: '60px',
    slidesToShow: 3,
    respondTo: 'slider',
    swipeToSlide: true,
    focusOnSelect: true,
    prevArrow: '<svg class="slick-prev slick-arrow"><line class="arrow" x1="100%" y1="0%" x2="0%" y2="50%"/><line class="arrow" x1="0%" y1="50%" x2="100%" y2="100%"/></svg>',
    nextArrow: '<svg class="slick-next slick-arrow"><line class="arrow" x1="0%" y1="0%" x2="100%" y2="50%"/><line class="arrow" x1="100%" y1="50%" x2="0%" y2="100%"/></svg>'
  })
  $('#info').slick({
    initialSlide: (window.totalElements / 2 >> 0),
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: false,
    fade: true,
    asNavFor: '#weekview'
  });

  $('#weekview').on('beforeChange', function(event, slick, currentSlide, nextSlide) {
    console.log(currentSlide);
    console.log(nextSlide);
    var diff = nextSlide - currentSlide;
    var date = new Date();
    date.setDate(window.currentDate.getDate() + diff);
    refresh(date, nextSlide);
  });
   
  window.currentDate = new Date(2017, 3, 25);
  refresh(window.currentDate, (window.totalElements / 2) >> 0);
});


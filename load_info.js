function refresh(date, forward) {
  document.currentDate = date;
  getInfo(date, function(results) {
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
      } else {
        // Add new slides
        // If we insert at the beginning all slides get shifted to the right but we need to make sure the current slide doesn't change
        if (!forward) {
          $('#weekview')[0].slick.currentSlide += 1;
          $('#info')[0].slick.currentSlide += 1;
        }
        $('#weekview').slick('slickAdd', newWeekviewElement(full_date), !forward);
        $('#info').slick('slickAdd', newDisplayElement(full_date), !forward);

        // Populate all the info
        dots = newDots(result['days'].length);
        document.getElementById(weekview_id).innerHTML = '<span>' + WEEKDAYS[result['dow']] + '<br/>' + result['raw_date'].getDate() + '<br/>' + dots + '</span>';
        info_element = document.getElementById(element_id);
        populateElement(info_element, result);
      }
    }
    // TODO: delete elements that are not found in the results to reduce cruft
  });
}

$(document).ready(function() {
  // Set up slider
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
    fade: true
  });

  // Initialize actual slides based on today's date
  document.currentDate = new Date();
  document.prevSlide = 0;
  refresh(document.currentDate, true);

  // Initialize to middle of the slider, don't animate, setup nav coordination after initial slide movement
  $('#info').slick('slickGoTo', (totalElements / 2 >> 0), true);
  $('#weekview').slick('slickGoTo', (totalElements / 2 >> 0), true);
  $('#info').slick('slickSetOption', {'asNavFor': '#weekview'});

  // Add event handlers for updating days as people move through the calendar
  $('#weekview').on('beforeChange', function(event, slick, currentSlide, nextSlide) {
    // afterChange doesn't have access to the slide before
    document.prevSlide = Number(currentSlide);
  });
  $('#weekview').on('afterChange', function(event, slick, currentSlide) {
    var diff = currentSlide - document.prevSlide;
    var date = new Date(document.currentDate.getTime());
    date.setDate(date.getDate() + diff);
    refresh(date, currentSlide > document.prevSlide);
  });

  // Add Google Analytics tracking for buttons
  $('#weekview').on('click', '.slick-arrow.slick-prev', function() {
    mixpanel.track('Click', {
      'target': 'prevarrow',
    });
  });
  $('#weekview').on('click', '.slick-arrow.slick-next', function() {
    mixpanel.track('Click', {
      'target': 'nextarrow',
    });
  });
  // Add Google Analytics tracking for dates
  $('#weekview').on('click', 'div.weekday-bubble', function(event) {
    mixpanel.track('Click', {
      'target': 'date',
      'date': $(this).attr('id'),
    });
  })
});


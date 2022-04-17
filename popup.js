// Google Analytics code
var _gaq = _gaq || [];
_gaq.push(['_setAccount', 'UA-98193595-1']);
_gaq.push(['_trackPageview', document.location.pathname]);

function load(date) {
  getInfo(date, function(results) {
    for (var i = 0; i < results.length; i++) {
      var result = results[i];
      if (getFullDate(result['raw_date']) == getFullDate(date)) {
        full_date = getFullDate(result['raw_date']);
        element_string = newDisplayElement(full_date);
        parent = document.getElementById('info');
        parent.innerHTML = element_string;
        element_id = 'info' + full_date;
        element = document.getElementById(element_id);
        populateElement(element, result);
      }
    }
  });
}

$(document).ready(function() {
  load(new Date());
});

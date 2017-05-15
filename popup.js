// Google Analytics code
var _gaq = _gaq || [];
_gaq.push(['_setAccount', 'UA-98193595-1']);
// _gaq.push(['_trackPageview']); TODO make this track popup views

(function() {
  var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
  ga.src = 'https://ssl.google-analytics.com/ga.js';
  var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
})(); 

function load(date) {
  var window = chrome.extension.getBackgroundPage();
  window.getInfo(date, function(results) {
    for (var i = 0; i < results.length; i++) {
      var result = results[i];
      if (window.getFullDate(result['raw_date']) == window.getFullDate(date)) {
        console.log('made it!');
        full_date = window.getFullDate(result['raw_date']);
        element_string = window.newDisplayElement(full_date);
        parent = document.getElementById('info');
        parent.innerHTML = element_string;
        element_id = 'info' + full_date;
        element = document.getElementById(element_id);
        window.populateElement(element, result);
      }
    }
  });
}

$(document).ready(function() {
   // Set saved color background immediately
  chrome.storage.local.get("backgroundColor", function(items) {
    backgroundColor = items.backgroundColor ? items.backgroundColor : DEFAULT_BACKGROUND_COLOR;
    document.body.style.backgroundColor = backgroundColor;
  });
  load(new Date());
});

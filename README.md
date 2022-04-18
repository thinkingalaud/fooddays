# fooddays
New tab page for Chrome that shows the current food day in the US

![screenshot](https://raw.githubusercontent.com/ihurrahi/fooddays/master/images/screenshot1.png "Screenshot")

## Dependencies
* jquery 1.7.0
** http://code.jquery.com/jquery-1.7.min.js
* slick 1.6.0
  * https://cdnjs.com/libraries/slick-carousel/1.6.0
    * ajax-loader.gif
    * slick-theme.min.css
    * slick-theme.min.css.map
    * slick.min.css
    * slick.min.css.map
    * slick.min.js

## Setup
* if a venv hasn't been set up yet, set one up: `python -m venv .venv`
* install deps: `python3 -m pip install -r requirements.txt`
* see `scripts/README.md` for information on how to refresh data
* load extension: go to `chrome://extensions/` and click on "Load Unpacked"

## Testing
* load extension: go to chrome://extensions and click "Load Unpacked"
* make sure the external dependencies above are downloaded and in the right directories

## Deployment
* update version number in manifest.json
* make sure you the dependencies installed and in the right directories
* create zip file
* upload package to the [dev console](https://chrome.google.com/webstore/devconsole)

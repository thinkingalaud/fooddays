# fooddays
New tab page for Chrome that shows the current food day in the US

![screenshot](https://raw.githubusercontent.com/ihurrahi/fooddays/master/images/screenshot1.png "Screenshot")

## Dependencies
* jquery 1.7.0
* slick 1.6.0

## Setup
* if a venv hasn't been set up yet, set one up: `python3 -m venv .venv`
* install deps: `python3 -m pip install -r requirements.txt`
* see `scripts/README.md` for information on how to refresh data
* load extension: go to `chrome://extensions/` and click on "Load Unpacked"

## Testing
* go to chrome://extensions and click Load Unpacked
* make sure you the dependencies installed and in the right directories

## Deployment
* update version number in manifest.json
* make sure you the dependencies installed and in the right directories
* create zip file
* upload package to the [dev console](https://chrome.google.com/webstore/devconsole)

#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import requests
from collections import defaultdict
from HTMLParser import HTMLParser

def read_data():
  res = []
  with open('data.js') as f:
    jstr = ''
    for line in f:
      if line.startswith('var') or line.startswith('`'):
        continue
      jstr += line
      if line.startswith('}'):
        res.append(json.loads(jstr))
        jstr = ''
  return res
cache, img_cache = read_data()

DATA_URL = "https://en.wikipedia.org/wiki/List_of_food_days"
SECRETS_FILE = '.secrets'

def load_secrets():
  with open(SECRETS_FILE, 'r') as f:
    secrets = json.load(f)
  return secrets

def get_food_image(date, food_day):
  """
  Google image search - 100 searches per day.
  https://developers.google.com/image-search/
  """
  secrets = load_secrets()
  url = 'https://www.googleapis.com/customsearch/v1?num=1&start=1&searchType=image&imgSize=xlarge&q=%s&cx=%s&key=%s' % (food_day, secrets['cx'], secrets['key'])
  res = requests.get(url)
  if res.status_code != 200:
    print "%s,%s returned:" % (date, food_day)
    print res
  else:
    first_res = res.json()['items'][0]
    image_url = first_res['link']
    width = int(first_res['image']['width'])
    height = int(first_res['image']['height'])
    if width and height:
      return image_url
  return None

def load_info():
  new_img_cache = dict((key, value) for key, value in img_cache.items() if value is not None)
  for date in cache:
    for day in cache[date]:
      key = ",".join([date, day])
      if key not in new_img_cache:
        result = get_food_image(date, day)
        new_img_cache[key] = result
  print json.dumps(new_img_cache)

def generate_picture_table():
  res = u"<html><body><table border=\"1\"><tr><th>Date</th><th>Day</th><th>Image</th></tr>"
  for key, src in sorted(img_cache.items()):
    date, day = key.split(',', 1)
    res += "<tr><td>%s</td><td>%s</td><td><img src=\"%s\"/ height=\"100\" width=\"100\"></td></tr>" % (date, day, src)
  res += "</table></body></html>"
  with open('test.html', 'wb') as f:
    f.write(res.encode('utf-8'))

class FoodDaysHTMLParser(HTMLParser):
  BLACKLIST_CATEGORIES = ['See also', 'References']

  def __init__(self):
    HTMLParser.__init__(self)
    self.result = {}
    self.h2 = False
    self.category = None
    self.table = self.thead = self.tbody = self.tr = self.th = self.td = False
    self.headers = []
    self.row = [""]

  def handle_starttag(self, tag, attrs):
    attrs = dict(attrs)
    if tag == 'h2':
      self.h2 = True
    if tag == 'span' and self.h2 and attrs.get('class') == 'mw-headline':
      self.category = None
    if tag in {'table', 'tr', 'th', 'td'}:
      setattr(self, tag, True)
    if tag == 'table':
      self.headers = []
    if tag == 'tr':
      self.row = [""]

  def handle_endtag(self, tag):
    if tag == 'h2':
      self.h2 = False
    if self.category == None:
      self.category = False
    if tag == 'tr' and len(self.headers) > 0 and len(self.row) > 1:
      row = dict(zip(self.headers, self.row[:-1]))
      self.result[self.category][row['Date']].append(row['Event'])
    if tag == 'td':
      self.row.append("")
    if tag in {'table', 'tr', 'th', 'td'}:
      setattr(self, tag, False)

  def handle_data(self, data):
    if self.h2 and self.category is None and data not in FoodDaysHTMLParser.BLACKLIST_CATEGORIES:
      self.category = data
      self.result[self.category] = defaultdict(lambda: list(""))
    if self.table and self.tr and self.th:
      self.headers.append(data)
    if self.table and self.tr and self.td:
      self.row[-1] += data.replace('\n', ' ')

def parse_wiki_page():
  wiki_res = requests.get(DATA_URL)
  parser = FoodDaysHTMLParser()
  parser.feed(wiki_res.text)
  res = dict((k, dict(v)) for k, v in parser.result.items())
  return res

#load_info()
#generate_picture_table()
#print json.dumps(parse_wiki_page(), indent=2)

# Old functions written in JS, originally was going to make the requests on the fly, but decided
# it would be too slow and less reliable. Also, most of it is duplicated by https://github.com/ihurrahi/shouldipigout
"""
function addRowData(storage, date, day) {
  if (date in storage) {
    storage[date].push(day);
  } else {
    storage[date] = [day];
  }
}

function getRawData(callback) {
  var xhr = new XMLHttpRequest();
  xhr.open("GET", DATA_URL);
  xhr.onload = function() {
    var result = this.responseText;
    var el = document.createElement('html');
    el.innerHTML = result;
    allContent = el.getElementsByClassName('mw-body-content');
    var res = {};
    for (var i = 0; i < allContent.length; i++) {
      content = allContent[i];
      for (var j = 0; j < content.children.length; j++) {
        var child = content.children[j];
        if (child.innerHTML.includes('United States')) {
          usSection = false;
          for (var k = 0; k < child.children.length; k++) {
            var grandchild = child.children[k];
            if (grandchild.tagName == 'H2') {
              if (grandchild.innerText.includes('United States')) {
                usSection = true;
              } else {
                usSection = false;
              }
            }
            if (usSection) {
              if (grandchild.tagName == 'H3') {
                currentMonth = grandchild.getElementsByTagName('span')[0].innerText;
              } else if (grandchild.tagName == 'TABLE') {
                rows = grandchild.getElementsByTagName('tr');
                for (var l = 0; l < rows.length; l++) {
                  row = rows[l];
                  rowData = row.getElementsByTagName('td');
                  if (rowData.length > 0) {
                    date = rowData[0].innerText;
                    monthFound = false;
                    for (var x = 0; x < MONTHS.length; x++) {
                      if (date.includes(MONTHS[x])) {
                        monthFound = true;
                      }
                    }
                    if (!(monthFound)) {
                      date = date + " of " + currentMonth;
                    }
                    addRowData(res, date, rowData[1].innerText);
                  }
                }
              }
            }
          }
        }
      }
    }
    callback(res);
  }
  xhr.onerror = function() {
    console.log('Encountered network error while getting raw data.');
    callback('');
  }
  xhr.send();
}
"""

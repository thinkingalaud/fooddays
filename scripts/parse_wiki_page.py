#!/usr/bin/python
import json
import re
import requests
from collections import defaultdict
from html.parser import HTMLParser

DATA_URL = "https://en.wikipedia.org/wiki/List_of_food_days"

class FoodDaysHTMLParser(HTMLParser):
  BLACKLIST_CATEGORIES = ['See also', 'References']

  def __init__(self):
    HTMLParser.__init__(self)
    self.result = defaultdict(list)
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
      self.result[row['Date'].strip()].append([row['Event'].strip(), self.category])
    if tag == 'td':
      self.row.append("")
    if tag in {'table', 'tr', 'th', 'td'}:
      setattr(self, tag, False)

  def handle_data(self, data):
    if self.h2 and self.category is None and data not in FoodDaysHTMLParser.BLACKLIST_CATEGORIES:
      if data == 'Global or International':
        data = 'Global'
      self.category = data
    if self.table and self.tr and self.th:
      self.headers.append(data.strip())
    if self.table and self.tr and self.td:
      self.row[-1] += re.sub('\[.*\]', '', data.replace('\n', ' ').replace('"', '\''))

def parse_wiki_page():
  wiki_res = requests.get(DATA_URL)
  parser = FoodDaysHTMLParser()
  parser.feed(wiki_res.text)
  return parser.result

def generate_cache():
  result = parse_wiki_page()
  print(json.dumps(result, sort_keys=True, indent=2, separators=(',', ': ')))

generate_cache()


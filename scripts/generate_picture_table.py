#!/usr/bin/python
import os
from shared import read_data, SCRIPTS

def generate_picture_table():
  cache, img_cache = read_data()
  res = u"<html><body><table border=\"1\"><tr><th>Date</th><th>Country</th><th>Day</th><th>Image</th></tr>"
  for date, days in sorted(cache.items()):
    for day, country in days:
      src = img_cache.get(date + ',' + day, '')
      res += "<tr><td>%s</td><td>%s</td><td>%s</td><td><img src=\"%s\"/ height=\"100\" width=\"100\"></td></tr>" % (date, country, day, src)
  res += "</table></body></html>"
  with open(os.path.join(SCRIPTS, 'test.html'), 'wb') as f:
    f.write(res.encode('utf-8'))

generate_picture_table()

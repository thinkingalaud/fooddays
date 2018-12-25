#!/usr/bin/python
from shared import read_data

def generate_picture_table():
  cache, img_cache = read_data()
  res = u"<html><body><table border=\"1\"><tr><th>Date</th><th>Country</th><th>Day</th><th>Image<    /th></tr>"
  for date, days in sorted(cache.items()):
    for day, country in days:
      src = img_cache[date + ',' + day]
      res += "<tr><td>%s</td><td>%s</td><td>%s</td><td><img src=\"%s\"/ height=\"100\" width=\"10    0\"></td></tr>" % (date, country, day, src)
  res += "</table></body></html>"
  with open('test.html', 'wb') as f:
    f.write(res.encode('utf-8'))


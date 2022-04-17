#!/usr/bin/python
import json
import requests

from shared import load_secrets, read_data

def get_food_image(date, food_day):
  """
  Google image search - 100 searches per day.
  https://developers.google.com/custom-search
  """
  secrets = load_secrets()
  # cx is the required search engine id, manage search engines at https://programmablesearchengine.google.com/
  # key is the required custom search api key, manage api keys at https://console.cloud.google.com/apis/credentials
  url = 'https://www.googleapis.com/customsearch/v1?num=1&start=1&searchType=image&imgSize=xlarge&q=%s&cx=%s&key=%s' % (food_day, secrets['GOOGLE_SEARCH_ENGINE_ID'], secrets['GOOGLE_SEARCH_API_KEY'])
  res = requests.get(url)
  if res.status_code != 200:
    print("%s,%s returned:" % (date, food_day))
    print(res.text)
  else:
    first_res = res.json()['items'][0]
    image_url = first_res['link']
    width = int(first_res['image']['width'])
    height = int(first_res['image']['height'])
    if width and height:
      return image_url
  return None

def generate(dry_run=True):
  cache, img_cache = read_data()
  new_img_cache = img_cache.copy()
  for date in cache: 
    for day, country in cache[date]:
      key = ",".join([date, day])
      if key not in new_img_cache:
        if dry_run:
          print('need new image for %s' % key)
        else:
          print('getting new image for %s' % key)
          result = get_food_image(date, day)
          new_img_cache[key] = result
  print(json.dumps(new_img_cache, indent=2))

generate(True)


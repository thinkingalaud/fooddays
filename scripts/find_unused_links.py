import json
from shared import read_data

def find_unused_links():
  cache, img_cache = read_data()
  for key, values in cache.items():
    for value in values:
      img_key = key + ',' + value[0]
      if img_key in img_cache:
        del img_cache[img_key]
  return img_cache

def without_unused_links():
  unused_links = find_unused_links()
  cache, img_cache = read_data()
  for key in unused_links:
    del img_cache[key]
  return img_cache

print json.dumps(find_unused_links(), indent=2, sort_keys=True)


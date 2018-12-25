#!/usr/bin/python
from imgurpython import ImgurClient
from imgurpython.helpers.error import ImgurClientRateLimitError

from shared import load_secrets

def get_imgur_client():
  # visit https://api.imgur.com/oauth2/authorize?client_id=77fbcca7c596528&response_type=token
  # to regenerate access token and refresh token and save in the secrets file
  secrets = load_secrets()
  client = ImgurClient(secrets['IMGUR_CLIENT_ID'], secrets['IMGUR_CLIENT_SECRET'], secrets['IMGUR    _ACCESS_TOKEN'], secrets['IMGUR_REFRESH_TOKEN'])
  return client

def upload_to_imgur():
  client = get_imgur_client()
  new_links = {}
  with open('images.txt') as f:
    images = json.loads(f.read())
  rate_limited = False
  for key, link in images.items():
    try:
      if 'imgur' in link or rate_limited:
        new_links[key] = link
      else:
        res = client.upload_from_url(link)
        print 'uploaded %s to %s' % (key, res['link'])
        new_links[key] = res['link']
    except ImgurClientRateLimitError as e:
      rate_limited = True
      print 'got rate limited'
      new_links[key] = link
    except:
      new_links[key] = link
  with open('images2.txt', 'w') as f:
    f.write(json.dumps(new_links))
  return new_links


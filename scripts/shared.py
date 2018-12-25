#!/usr/bin/python
import json

DATA_FILE = '../data.js'
SECRETS_FILE = '../.secrets'

def read_data():
  res = []
  with open(DATA_FILE) as f:
    jstr = ''
    for line in f:
      if line.startswith('var') or line.startswith('`'):
        continue
      jstr += line
      if line.startswith('}'):
        res.append(json.loads(jstr))
        jstr = ''
  return res

def load_secrets():
  with open(SECRETS_FILE, 'r') as f:
    secrets = json.load(f)
  return secrets


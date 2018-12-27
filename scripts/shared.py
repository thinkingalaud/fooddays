#!/usr/bin/python
import json
import os

# Assume root path is 2 levels above this file
SCRIPTS = os.path.abspath(os.path.dirname(__file__))
ROOT = os.path.abspath(os.path.dirname(SCRIPTS))
DATA_FILE = os.path.join(ROOT, 'data.js')
SECRETS_FILE = os.path.join(ROOT, '.secrets')

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


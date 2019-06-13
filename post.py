import json
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

url = 'http://192.168.11.25:5000/'
data = {
  'score':{
    'time': 12345,
    'miss': 12345,
    'score': 99998,
    'name': 'test',
  }
}
headers = {
    'Content-Type': 'application/json',
}

req = urllib.request.Request(url, json.dumps(data).encode(), headers)
with urllib.request.urlopen(req) as res:
    body = res.read()
import json
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

url = 'http://192.168.100.25:5000/'
data = {
  'score':{
    'time': 987654321,
    'miss': 987654321,
    'score': 987654321,
    'name': 'test',
  }
}
headers = {
    'Content-Type': 'application/json',
}

req = urllib.request.Request(url, json.dumps(data).encode(), headers)
with urllib.request.urlopen(req) as res:
    body = res.read()
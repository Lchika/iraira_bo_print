# coding: utf-8

from flask import *
import json
import urllib.request
import ssl

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def handle_root():
  if request.method == "GET":
    return 'IBPS(Iraira Bo Print Server) is running'
  else:
    if request.headers['Content-Type'] != 'application/json':
        print(request.headers['Content-Type'])
        return jsonify(res='error'), 400

    ssl._create_default_https_context = ssl._create_unverified_context
    url = 'https://lchika.club/scores'
    headers = {
      'Content-Type': 'application/json',
    }
    req = urllib.request.Request(url, json.dumps(request.json).encode(), headers)
    with urllib.request.urlopen(req) as res:
      res.read()
    return 'score was sent'

if __name__ == '__main__':
  app.run()
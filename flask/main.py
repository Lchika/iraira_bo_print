#!/usr/bin/python -u
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
    comm_path = '/home/pi/work/iraira/iraira_bo_print/comm.txt'
  
    if request.headers['Content-Type'] != 'application/json':
        print(request.headers['Content-Type'])
        return jsonify(res='error'), 400

    ssl._create_default_https_context = ssl._create_unverified_context
    url = 'https://lchika.club/scores'
    headers = {
      'Content-Type': 'application/json',
    }
    app.logger.info(request.json)
    req = urllib.request.Request(url, json.dumps(request.json).encode(), headers)
    with urllib.request.urlopen(req) as res:
      res.read()
    with open(comm_path, mode='a') as f:
      f.write(json.dumps(request.json) + '\n')
    return 'score was sent'

if __name__ == '__main__':
  app.run("0.0.0.0", debug=True)
  #app.run("0.0.0.0")

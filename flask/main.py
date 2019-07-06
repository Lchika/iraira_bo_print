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
    url_score_site = 'https://lchika.club/scores'
    url_result_server = 'http://192.168.100.111'
    headers = {
      'Content-Type': 'application/json',
    }
    app.logger.info(request.json)
    req = urllib.request.Request(url_score_site, json.dumps(request.json).encode(), headers)
    with urllib.request.urlopen(req) as res:
      res_html = res.read().decode('utf-8')
      print('score_site res=' + res_html)
    req = urllib.request.Request(url_result_server, json.dumps(request.json).encode(), headers)
    try:
      with urllib.request.urlopen(req) as res:
        res_html = res.read().decode('utf-8')
        print('result_sserver res=' + res_html)
    except:
      app.logger.info('Error: failed to request to result server')
    with open(comm_path, mode='a') as f:
      f.write(json.dumps(request.json) + '\n')
    return 'score was sent'

if __name__ == '__main__':
  app.run("0.0.0.0", debug=True)
  #app.run("0.0.0.0")

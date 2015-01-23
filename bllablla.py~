from flask import Flask
from flask import Response, render_template, request, json
import urllib2
from urllib2 import urlopen
from bson import json_util, SON
import argparse


app = Flask(__name__)

@app.route("/")
def index():
    url = "http://0.0.0.0:5030/display/events"
    result = urlopen(url).read()
    json_result = json.loads(result)

    url1 = "http://0.0.0.0:5030/display/volunteer"
    result1 = urlopen(url1).read()
    json_result1 = json.loads(result1)

    return render_template("event.html", result=json_result, result1=json_result1)



@app.route("/create/event", methods=['POST'])
def create_event():
    url = 'http://0.0.0.0:5030/create/event'
    data = request.data

    print data
    json_doc = {}

    json_string = request.data
    
    r = urllib2.Request(url, data=json_string, headers={"Content-Type": "application/json"})
    res = urllib2.urlopen(r)
    
    resp = Response(
        response=data,
        mimetype='application/json')
    return resp
    #TODO: return json_response

@app.route("/register/volunteer", methods=['POST'])
def register_volunteer():
    url = 'http://0.0.0.0:5030/register/volunteer'
    data = request.data

    print data
    json_string = request.data
    
    r = urllib2.Request(url, data=json_string, headers={"Content-Type": "application/json"})
    res = urllib2.urlopen(r)
    

    resp = Response(
        response=data,
        mimetype='application/json')
    return resp

if __name__ == '__main__':
    app.run(debug=True)

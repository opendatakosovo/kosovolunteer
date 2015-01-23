from flask import Flask
from flask.views import View
from flask import Response, render_template, request, json
import urllib2
from bson import json_util, SON
from ve import utils
import argparse

class CreateEvent(View):
    
    def dispatch_request(self):

        api_base_url = utils.get_api_url()
        url = '%s/create/event'%(api_base_url)
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

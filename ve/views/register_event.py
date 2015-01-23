from flask import Flask
from flask.views import View
from flask import Response, request
import urllib2
from ve import utils


class RegisterEvent(View):
    def dispatch_request(self):
        api_base_url = utils.get_api_url()
        url = '%s/register/volunteer'%(api_base_url)
        data = request.data

        print data
        json_string = request.data
        
        r = urllib2.Request(url, data=json_string, headers={"Content-Type": "application/json"})
        res = urllib2.urlopen(r)
        

        resp = Response(
        response=data,
        mimetype='application/json')
        return resp

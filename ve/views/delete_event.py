from flask import Flask
from flask.views import View
from flask import Response, request
import urllib2
from ve import utils

class DeleteEvent(View):
    def dispatch_request(self):
        api_base_url = utils.get_api_url()
        
        url = '%s/delete/event' % (api_base_url)
        data = request.data
        
        r = urllib2.Request(url, data=data, headers={"Content-Type": "application/json"})
        res = urllib2.urlopen(r)
        
        resp = Response(status=200, mimetype='application/json')      
        return resp
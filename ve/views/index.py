from flask import render_template
from flask.views import View
from urllib2 import urlopen
from ve import utils
import json

class Index(View):
    def dispatch_request(self):
        api_base_url = utils.get_api_url()
        url = "%s/display/events" %(api_base_url)
        result = urlopen(url).read()
        json_result = json.loads(result)

        url1 = "%s/display/volunteer"%(api_base_url)
        result1 = urlopen(url1).read()
        json_result1 = json.loads(result1)

        return render_template("event.html", result=json_result, result1=json_result1)

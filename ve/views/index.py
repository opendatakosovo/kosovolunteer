from flask import render_template
from flask.views import View
from urllib2 import urlopen
from ve import utils
import json

class Index(View):
    def dispatch_request(self):
        api_base_url = utils.get_api_url()
        url = "%s/display/events" %(api_base_url)
        DisplayEvents = urlopen(url).read()
        json_result = json.loads(DisplayEvents)

        url1 = "%s/display/volunteer"%(api_base_url)
        DisplayVolunter = urlopen(url1).read()
        json_result1 = json.loads(DisplayVolunter)

        return render_template("event.html", DisplayEvents=json_result, DisplayVolunter=json_result1)

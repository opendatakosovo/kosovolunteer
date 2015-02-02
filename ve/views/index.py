from flask import render_template
from flask.views import View
from urllib2 import urlopen
from ve import utils
import json

class Index(View):
    def dispatch_request(self):
    	api_base_url = utils.get_api_url()
        url = "%s/display/events" % (api_base_url)

        events_str = urlopen(url).read()

        events = json.loads(events_str)

        return render_template("index.html", events=events)

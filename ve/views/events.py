from flask import render_template
from flask.views import View
from urllib2 import urlopen
from ve import utils
import json

class Events(View):
    def dispatch_request(self):
        api_base_url = utils.get_api_url()
        url = "%s/display/events" %(api_base_url)

        events = urlopen(url).read()
        events_json = json.loads(events)

        return render_template("events.html", events=events_json)

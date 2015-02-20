from flask import render_template
from flask.views import View
from urllib2 import urlopen
from ve import utils
import json

class Index (View):
    def dispatch_request(self):
       return render_template("index.html")

# -*- encoding: utf-8 -*-
# Author: Epix
import json
import time

import requests

from atcrawler.info import *

req_json_file = open('offline/req_json.jl', 'r')
for line in req_json_file:
    req_json = json.loads(line.strip())
    r = requests.post(ARIA_URL, data=line.strip())
    time.sleep(0.08)

#!/usr/bin/env python

import os
import sys
import requests
import anyconfig
from datetime import datetime, timedelta
import json

# Getting url of the api to call
config = anyconfig.load('data.yml')
if config is None or 'baseurl' not in config:
        print "Error parsing yaml"
        exit(1)

baseurl = config['baseurl']
listurl = baseurl + '/api/list'

# Getting timestamp of 4 days in past
now = datetime.now()
prev = now - timedelta(1)
ts = (prev - datetime(1970, 1, 1)).total_seconds()

# Adding the timestamp to payload
payload = {}
payload['timestamp'] = ts

# Sending the request
resp = requests.post(listurl, data=payload)
if resp.status_code != 200:
        print "Error received : " + str(resp.status_code)
        exit(2)
else:
        cntnt = json.loads(resp.content)
        print json.dumps(cntnt, indent=2, sort_keys=True)

#!/usr/bin/env python

import os
import sys
import requests
import anyconfig
from datetime import datetime, timedelta
import json

def get_news_dict(ts=None):
        """Returns a dict containing list of editorials after timestamp ts. By
        default, the difference is mentioned as 'default_offset' in data.yml."""

        # Getting url of the api to call from data.yml file
        config = anyconfig.load('data.yml')
        if config is None or 'baseurl' not in config or 'default_offset' not in config:
                print "Error parsing yaml"
                return None

        baseurl = config['baseurl']
        listurl = baseurl + '/api/list'

        # Getting timestamp of default offset as mentioned in data.yml
        if ts is None:
                doff = config['default_offset']
                now = datetime.now()
                prev = now - timedelta(doff)
                ts = (prev - datetime(1970, 1, 1)).total_seconds()

        # Adding the timestamp to payload
        payload = {}
        payload['timestamp'] = ts

        # Sending the request
        resp = requests.post(listurl, data=payload)

        # Analysing the response
        if resp.status_code != 200:
                print "Error received : " + str(resp.status_code)
                return None
        else:
                cntnt = json.loads(resp.content)
                return cntnt

if __name__ == '__main__':
        news_dict = get_news_dict()
        if news_dict is not None:
                # Pretty print the dictionary received
                print json.dumps(news_dict, indent=2, sort_keys=True)

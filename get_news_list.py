#!/usr/bin/env python

import os
import sys
import requests
import anyconfig

config = anyconfig.load('data.yml')
print config

#!/bin/bash/python
#
# file: grab_token.py
# abstract: Grabs token for authenticated session, using client
#

import sys
from selenium import webdriver
import tda

# Make a webdriver binding -- going with Chromium
#
# How to
# https://sites.google.com/chromium.org/driver/getting-started
#
# Driver download
# https://chromedriver.storage.googleapis.com/index.html
driver = webdriver.Chrome('./chromedriver')

try:
    api_key = str(sys.argv[1])
except:
    print("Please use your app's api key")

tda.auth.client_from_manual_flow(api_key, 'https://localhost', './token')
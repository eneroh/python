#!/bin/python

###
mass_requests_to_scan_site.py

based on video by engineer man: 
###

import requests
import threading

url = '<scam site>'

data = {
  REVIEW additional information via chrome console or similar when capturing request
  'cc_number': '4007000000027',
  'cc_expmonth': '08',
  'cc_expyear': '21',
  'cc_cvv': '234'
}

def do_request():
  while true:
    response = requests.post(url,data=data).text
    print(response)

threads = []

for i in range(50):
  t = threading.Thread(target=do_request)
  t.daemon = True
  threads.append(t)

for i in range(50):
  threads[i].start()

for i in range(50):
  threads[i].join()

# test program at this point

error occurs if you do not add all the additional form information

# takes 2 secs with the above but add threading to send many more


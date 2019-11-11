#!/usr/bin/env python
from __future__ import print_function
import time
import requests
import socket
from Core.colors import *

def getgeoip(web):

    web = web.replace('http://','')
    web = web.replace('https://','')
    print(R+'\n   =========================')
    print(R+'    G E O I P   L O O K U P')
    print(R+'   =========================\n')
    time.sleep(0.4)
    print(GR+" [~] Found GeoIp Location: \n")
    domains = socket.gethostbyname(web)
    time.sleep(0.6)
    text = requests.get('http://api.hackertarget.com/geoip/?q={}'.format(domains)).text
    result = str(text)
    longitude = ""
    latitude = ""
    if 'error' not in result and 'invalid' not in result:
        res = result.splitlines()
        for r in res:
            if r.startswith("Longitude"):
                longitude = r.split(':')[1].strip()
            if r.startswith("Latitude"):
                latitude = r.split(':')[1].strip()
            print(G+' [+] ' + r.split(':')[0].strip() + ' : ' +O+ r.split(':')[1].strip())
            time.sleep(0.1)
        place = "the aproximate location of the ip: https://www.google.com/maps/?q={},{}".format(latitude, longitude)
        print(place)

    else:
        print(R+' [-] Outbound Query Exception!')
        time.sleep(0.8)

target = input("IP of Target: ")
getgeoip(web=target)

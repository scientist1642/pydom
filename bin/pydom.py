#!/usr/bin/python -tt

import urllib
import urllib2
import json
import sys
import termcolor

YES_COLOR = 'green'
NOT_COLOR = 'red'
MAYBE_COLOR = 'yellow'
NON_COLOR = 'white'

def domainr_search_json(domainname = 'www.geolymp.org'):
    requesturl = 'http://www.domai.nr/api/json/search?q='
    requesturl += domainname
    request = urllib2.Request(requesturl)
    request.add_header('User-Agent', 'domainr.py/0.1')
    opener = urllib2.build_opener()
    response = opener.open(request).read()
    objs = json.loads(response)
    return objs

def choose_color(aval):
    if aval == 'taken' or aval == 'unavailable':
        return NOT_COLOR
    elif aval == 'maybe':
        return MAYBE_COLOR
    elif aval == 'available':
        return YES_COLOR
    else:
        return NON_COLOR

def main():
    domainr_objs = domainr_search_json(sys.argv[1])
    for item in domainr_objs['results']:
        domain = item['domain']
        availability = item['availability']
        print termcolor.colored(domain + ' ' + availability, 
                choose_color(availability))

if __name__ == '__main__':
    main()

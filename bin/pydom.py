#!/usr/bin/python -tt

import urllib
import urllib2
import json
import sys
import termcolor

YES_COLOR = 'green'
NOT_COLOR = 'red'
MAYBE_COLOR = 'yellow'

def domainr_search_json(domainname = 'www.geolymp.org'):
    requesturl = 'http://www.domai.nr/api/json/search?q='
    requesturl += domainname
    request = urllib2.Request(requesturl)
    request.add_header('User-Agent', 'domainr.py/0.1')
    opener = urllib2.build_opener()
    response = opener.open(request).read()
    objs = json.loads(response)
    return objs

def main():
    domainr_objs = domainr_search_json(sys.argv[1])
    for item in domainr_objs['results']:
        domain = item['domain']
        
        availability = item['availability']

        if availability == 'taken':
            col =  NOT_COLOR
        elif availability == 'maybe':
            col = MAYBE_COLOR
        else:
            col = YES_COLOR
        print termcolor.colored(domain + ' ' + availability, col)

if __name__ == '__main__':
    main()

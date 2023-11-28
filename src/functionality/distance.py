"""
MIT License

Copyright (c) 2023 SEGroup10

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 01:41:59 2021

@author: anant
"""
import os
import requests
import sys
import json
#import config

def get_key():
    '''
    Function to extract API key

    Returns
    -------
    api_key_1 : reutrns the api key for google connection

    '''
    api_key_1=""
    key_data = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname
                                            (os.path.abspath(__file__)))), "json", "key.json")
    if not os.path.exists(key_data):
        print(
            '''Api Key file does not exist. Please refer to readme to add key and restart program''')
        sys.exit("Thank you for using ScheduleBot")
    with open(key_data) as json_file:
        data = json.load(json_file)
        api_key_1 = data["key"]
    return api_key_1
    
def get_lat_log( address,api_key_1):
    """
    This function converts a textual address to a set of coordinates

    address : String
        the location for which coordinates are needed.

    Returns
    -------
    list
        the latitude and longitude of the given address using google maps.

    """
    address2 = address.replace(" ", "+")
    url = '''https://maps.googleapis.com/maps/api/geocode/json?key={0}&address={1}&language=en-EN'''.format(api_key_1, str(address2))
    r = requests.get(url)
    print(url)
    print("\n\n\nlatlon")
    return [r.json().get("results")[0].
            get("geometry").
            get("location").
            get('lat'),
            r.json().get("results")[0].get("geometry").get("location").get('lng')]

def get_distance( dest, src,mode):
    """
    this gets the distace matrix which includes the travel time to the event

    Input:
    dest : Takes address of location for event as a string.
    src : Takes coordinates of source address as a list.
    mode: Takes Mode of transport as a string.

    Returns:
    travel time in seconds.

    """
    api_key_1=get_key()
    print(src)
    print(dest)
    print(mode)
    url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
    dest_lat_lon = get_lat_log(dest,api_key_1)
    src = get_lat_log(src,api_key_1)
    if dest_lat_lon is None:
        print("Location not Found")
        return 0
    orig = str(src[0]) + " " + str(src[1])
    dest = str(dest_lat_lon[0]) + " " + str(dest_lat_lon[1])
    url = '''https://maps.googleapis.com/maps/api/distancematrix/json?key={0}&origins={1}&destinations={2}&mode={3}&language=en-EN&sensor=false'''.format(
        api_key_1, str(orig), str(dest), mode)
    r = requests.get(url)
    print(url)
    print(r)
    travel_time = r.json().get('rows')[0].get("elements")[
        0].get("duration").get("value")
    print("Travel time:")
    print(travel_time)
    return travel_time

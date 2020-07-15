#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geojson.py. The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as within Google Maps.
#API End Points

#To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:

#http://py4e-data.dr-chuck.net/json?
#This API uses the same parameter (address) as the Google API. This API also has no rate limit so you can test as often as you like. If you visit the URL with no parameters, you get "No address..." response.
#To call the API, you need to include a key= parameter and provide the address that you are requesting as the address= parameter that is properly URL encoded using the urllib.parse.urlencode() function as shown in http://www.py4e.com/code3/geojson.py

#Make sure to check that your code is using the API endpoint is as shown above. You will get different results from the geojson and json endpoints so make sure you are using the same end point as this autograder is using.
import json
import urllib
import urllib.request,urllib.parse,urllib.error

serviceurl = "http://py4e-data.dr-chuck.net/json?"

while True:

    address = input('Enter Location')
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode({'key': 42, 'address': address})
    print('Retrieving:',url)
    url_info = urllib.request.urlopen(url).read().decode()

    try: js = json.loads(url_info)
    except: js = None

    print('Retrieved', len(url_info))
    print('Place_ID',js['results'][0]['place_id'])

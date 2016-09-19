import json
import urllib2

from api_key import my_key

if my_key=="Not a real key. Get yours at https://developers.google.com/maps/documentation/distance-matrix/get-api-key, then put it here." :
   print "FAIL! You need your own key from "
   print "   https://developers.google.com/maps/documentation/distance-matrix/get-api-key"
   print " Get a key, modify api_key.py to assign my_key. Then try again."
   exit()

start = raw_input("Enter origin city: ")
end = raw_input("Enter destination city: ")

url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial" + \
      "&key=" + my_key + \
      "&origins=" + "+".join(start.split(" ")) + \
      "&destinations=" + "+".join(end.split(" "))

#print url

resp=urllib2.urlopen(url).read()

output = json.loads(resp)
#print output
if output['status'] != 'OK':
   print "FAIL! No response from Google Maps API. Is that a real key?"
else:
   try:
      print "It takes "+ output['rows'][0]['elements'][0]['duration']['text'] + \
          " to get from " + \
          output['origin_addresses'][0] + " to " + \
          output['destination_addresses'][0] 
   except:
      print "FAIL! Bad output from API. Are those real places?"



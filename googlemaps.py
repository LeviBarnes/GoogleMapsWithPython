import json
import urllib2

from api_key import my_key

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
   print "FAIL!"
else:
   print "It takes "+ output['rows'][0]['elements'][0]['duration']['text'] + \
       " to get from " + \
       output['origin_addresses'][0] + " to " + \
       output['destination_addresses'][0] 



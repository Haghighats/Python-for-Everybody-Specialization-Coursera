import urllib.request as ur
import urllib.parse as up
import json

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'




Location_url = input ("Enter location: ")
params = {"sensor": "false", "address": Location_url}
url = serviceurl + up.urlencode(params)
print('Retrieving', url)

uh = ur.urlopen(url).read().decode()
print("Retrieved" , len(uh), "characters" )

info = json.loads(uh)
    

print(type(info))
place_id = info["results"][0]["place_id"]
print("Place_id:" , place_id)

#Universitat Politecnica de Valencia

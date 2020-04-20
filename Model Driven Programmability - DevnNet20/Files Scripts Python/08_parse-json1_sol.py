#Replace 'your_api_key' with your MapQuest API key

import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Washington"
dest = "Baltimaore"
key = "your_api_key"

url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})

json_data = requests.get(url).json()
print(json_data)

'''
OUTPUT:
{'route': {'distance': 38.089, 'hasHighway': True, 'hasUnpaved': False, 'hasAccessRestriction': False, 'options': {'mustAvoidLinkIds': [], 'maxWalkingDistance': -1, 'manmaps': 'true', 'urbanAvoidFactor': -1, 'stateBoundaryDisplay': True, 'cyclingRoadFactor': 1, 'routeType': 'FASTEST', 'countryBoundaryDisplay': True, 'drivingStyle': 2, 'highwayEfficiency': 22, 'narrativeType': 'text', 'routeNumber': 0, 'tryAvoidLinkIds': [], 'generalize': -1, 'returnLinkDirections': False, 'doReverseGeocode': True, 'avoidTripIds': [], 'timeType': 0, 'sideOfStreetDisplay': True, 'filterZoneFactor': -1, 'walkingSpeed': -1, 'useTraffic': False, 'unit': 'M', 'tr
[output omitted]
>>> 
'''

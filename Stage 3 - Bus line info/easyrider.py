# This is Amirhossein Jahazi AKA combat47
import json

bus_string = input()
bus_json = json.loads(bus_string)
buses_stops = {}

for i in range(0, len(bus_json)):
    if str(bus_json[i]['bus_id']) not in buses_stops:
        buses_stops[str(bus_json[i]['bus_id'])] = {str(bus_json[i]['stop_id']): str(bus_json[i]['stop_name'])}
    else:
        if ((str(bus_json[i]['stop_id']), str(bus_json[i]['stop_name']))
                not in buses_stops[str(bus_json[i]['bus_id'])].items()):
            buses_stops[str(bus_json[i]['bus_id'])][str(bus_json[i]['stop_id'])] = str(bus_json[i]['stop_name'])

print("Line names and number of stops:")
for i in buses_stops.keys():
    print("bus_id:" + str(i) + ", stops: " + str(len(buses_stops[i])))

# This is Amirhossein Jahazi AKA combat47
import json

on_demand = list()
other = list()
bus_string = input()
bus_json = json.loads(bus_string)
buses_stops = {}

for i in range(0, len(bus_json)):
    type_ = bus_json[i]['stop_type']
    name = bus_json[i]['stop_name']
    if type_ != "O":
        other.append(name)
    else:
        on_demand.append(name)

on_demand_errors = set(on_demand).intersection(set(other))

print("On demand stops test:")
if len(on_demand_errors) == 0:
    print("OK")
else:
    print("Wrong stop type: ", sorted(list(on_demand_errors)))

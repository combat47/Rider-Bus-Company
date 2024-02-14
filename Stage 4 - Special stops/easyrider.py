# This is Amirhossein Jahazi AKA combat47
import json

start = list()
end = list()
other = list()
transfer = list()

bus_string = input()
bus_json = json.loads(bus_string)
buses_stops = {}

for i in range(0, len(bus_json)):
    if bus_json[i]['stop_type'] == "S":
        if bus_json[i]['stop_name'] not in start:
            start.append(bus_json[i]['stop_name'])
            if bus_json[i]['stop_name'] in end or bus_json[i]['stop_name'] in other:
                transfer.append(bus_json[i]['stop_name'])
        else:
            transfer.append(bus_json[i]['stop_name'])
    elif bus_json[i]['stop_type'] == "F":
        if bus_json[i]['stop_name'] not in end:
            end.append(bus_json[i]['stop_name'])
            if bus_json[i]['stop_name'] in start or bus_json[i]['stop_name'] in other:
                transfer.append(bus_json[i]['stop_name'])
        else:
            transfer.append(bus_json[i]['stop_name'])
    else:
        if bus_json[i]['stop_name'] not in other:
            other.append(bus_json[i]['stop_name'])
            if bus_json[i]['stop_name'] in end or bus_json[i]['stop_name'] in start:
                transfer.append(bus_json[i]['stop_name'])
        else:
            transfer.append(bus_json[i]['stop_name'])

    if str(bus_json[i]['bus_id']) not in buses_stops:
        buses_stops[str(bus_json[i]['bus_id'])] = {str(bus_json[i]['stop_type']): str(bus_json[i]['stop_name'])}
    else:
        buses_stops[str(bus_json[i]['bus_id'])][str(bus_json[i]['stop_type'])] = str(bus_json[i]['stop_name'])

for i in buses_stops:
    if "S" not in buses_stops[i] or "F" not in buses_stops[i]:
        print("There is no start or end stop for the line: {}.".format(i))
        break

transfer1 = set(transfer)

print("Start stops: {} {}".format(len(start), sorted(start)))
print("Transfer stops: {} {}".format(len(transfer1), sorted(transfer1)))
print("Finish stops: {} {}".format(len(end), sorted(end)))

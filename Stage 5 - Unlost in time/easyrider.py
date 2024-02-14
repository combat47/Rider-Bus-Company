# This is Amirhossein Jahazi AKA combat47
import json

start = list()
end = list()
other = list()
transfer = list()

bus_string = input()
bus_json = json.loads(bus_string)

bus_num = list()
bus_station = list()


for i in range(0, len(bus_json) - 1):
    if bus_json[i]["bus_id"] == bus_json[i + 1]["bus_id"]:
        if bus_json[i]['next_stop'] != 0:
            if bus_json[i]['a_time'] >= bus_json[i + 1]['a_time']:
                if bus_json[i]["bus_id"] not in bus_num:
                    bus_num.append(bus_json[i + 1]['bus_id'])
                    bus_station.append(bus_json[i + 1]['stop_name'])

print("Arrival time test:")
if len(bus_num) == 0:
    print("OK")
else:
    for num, name in zip(bus_num, bus_station):
        print("bus_id line {}: wrong time on station {}".format(num, name))

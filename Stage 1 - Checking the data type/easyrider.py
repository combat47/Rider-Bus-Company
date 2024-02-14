# This is Amirhossein Jahazi AKA combat47
import json

errors = {'bus_id': 0, 'stop_id': 0, 'stop_name': 0, 'next_stop': 0, 'stop_type': 0, 'a_time': 0}
total = sum(errors.values())

bus_string = input()
bus_json = json.loads(bus_string)

for i in range(0, len(bus_json)):
    if type(bus_json[i]['bus_id']) is not int:
        errors['bus_id'] += 1
    if type(bus_json[i]['stop_id']) is not int:
        errors['stop_id'] += 1
    if type(bus_json[i]['stop_name']) is not str:
        errors['stop_name'] += 1
    elif bus_json[i]['stop_name'] == "":
        errors['stop_name'] += 1
    if type(bus_json[i]['next_stop']) is not int:
        errors['next_stop'] += 1
    if type(bus_json[i]['stop_type']) is not str:
        errors['stop_type'] += 1
    elif bus_json[i]['stop_type'] not in "SOF":
        errors['stop_type'] += 1
    if type(bus_json[i]['a_time']) is not str:
        errors['a_time'] += 1
    elif bus_json[i]['a_time'] == "":
        errors['a_time'] += 1

total = sum(errors.values())
print(f"Type and required field validation: {total} errors")
for i in errors:
    print(i + ": " + str(errors[i]))

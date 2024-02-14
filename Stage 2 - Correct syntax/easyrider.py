# This is Amirhossein Jahazi AKA combat47
import json
import re

errors = {'stop_name': 0, 'stop_type': 0, 'a_time': 0}
total = sum(errors.values())

bus_string = input()
bus_json = json.loads(bus_string)

for i in range(0, len(bus_json)):
    if type(bus_json[i]['stop_name']) is not str:
        errors['stop_name'] += 1
    elif bus_json[i]['stop_name'] == "":
        errors['stop_name'] += 1
    elif re.match("([A-Z][a-z]* )+(Road|Avenue|Boulevard|Street)$", bus_json[i]['stop_name']) is None:
        errors['stop_name'] += 1
    if type(bus_json[i]['stop_type']) is not str:
        errors['stop_type'] += 1
    elif bus_json[i]['stop_type'] not in "SOF":
        errors['stop_type'] += 1
    if type(bus_json[i]['a_time']) is not str:
        errors['a_time'] += 1
    elif bus_json[i]['a_time'] == "":
        errors['a_time'] += 1
    elif re.fullmatch("([0-1][0-9]|2[0-4]):([0-5][0-9])", bus_json[i]['a_time']) is None:
        errors['a_time'] += 1

total = sum(errors.values())
print(f"Format validation: {total} errors")
for i in errors:
    print(i + ": " + str(errors[i]))

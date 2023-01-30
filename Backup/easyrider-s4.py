# Easy Rider: Stage 4/6
# https://hyperskill.org/projects/128/stages/683/implement

import json

json_str = r'''[
    {
        "bus_id": 128,
        "stop_id": 1,
        "stop_name": "Prospekt Avenue",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": "08:12"
    },
    {
        "bus_id": 128,
        "stop_id": 3,
        "stop_name": "Elm Street",
        "next_stop": 5,
        "stop_type": "",
        "a_time": "08:19"
    },
    {
        "bus_id": 128,
        "stop_id": 5,
        "stop_name": "Fifth Avenue",
        "next_stop": 7,
        "stop_type": "O",
        "a_time": "08:25"
    },
    {
        "bus_id": 128,
        "stop_id": 7,
        "stop_name": "Sesame Street",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:37"
    },
    {
        "bus_id": 256,
        "stop_id": 2,
        "stop_name": "Pilotow Street",
        "next_stop": 3,
        "stop_type": "S",
        "a_time": "09:20"
    },
    {
        "bus_id": 256,
        "stop_id": 3,
        "stop_name": "Elm Street",
        "next_stop": 6,
        "stop_type": "",
        "a_time": "09:45"
    },
    {
        "bus_id": 256,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 7,
        "stop_type": "",
        "a_time": "09:59"
    },
    {
        "bus_id": 256,
        "stop_id": 7,
        "stop_name": "Sesame Street",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "10:12"
    },
    {
        "bus_id": 512,
        "stop_id": 4,
        "stop_name": "Bourbon Street",
        "next_stop": 6,
        "stop_type": "S",
        "a_time": "08:13"
    },
    {
        "bus_id": 512,
        "stop_id": 6,
        "stop_name": "Sunset Boulevard",
        "next_stop": 0,
        "stop_type": "F",
        "a_time": "08:16"
    }
]'''

#routes = json.loads(json_str)
routes = json.loads(input())
busses = {}
stops_all = {}
stops_start = set()
stops_finish = set()

for route in routes:
    busses.setdefault(route['bus_id'], set()).add(route['stop_type'])
    if route['stop_type'] == 'S':
        stops_start.add(route['stop_name'])
    if route['stop_type'] == 'F':
        stops_finish.add(route['stop_name'])
    stops_all.setdefault(route['stop_name'], 0)
    stops_all[route['stop_name']] += 1

stops_transfer = {stop for stop, count in stops_all.items() if count > 1}

for bus, stop_type in busses.items():
    if not {'S', 'F'} <= stop_type:
        print(f'There is no start or end stop for the line: {bus}')
        exit()

print(f'Start stops: {len(stops_start)} {sorted(list(stops_start))}')
print(f'Transfer stops: {len(stops_transfer)} {sorted(list(stops_transfer))}')
print(f'Finish stops: {len(stops_finish)} {sorted(list(stops_finish))}')

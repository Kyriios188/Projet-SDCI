import sys
import requests
import json
from time import sleep

ping_url = sys.argv[1]

values_list = []

while True:
    r = requests.get(url=ping_url)
    
    current_latency = r.json()['pong']
    values_list.append(int(current_latency))
    if len(values_list) > 10:
        values_list = values_list[1:]
    print(values_list)
    sleep(1)

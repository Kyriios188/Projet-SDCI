import sys
import requests
import json
from time import sleep


health_url = sys.argv[1]
values_list = []

while True:
    r = requests.get(url=health_url)
    
    current_health = r.json()['avgLoad']
    values_list.append(float(current_health))
    if len(values_list) > 10:
        values_list = values_list[1:]

    print(values_list)
    sleep(1)

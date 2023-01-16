import sys
import requests
import json


gwi_ip = sys.argv[1]
gwi_port = sys.argv[2]

health_url = "http://"+gwi_ip+":"+gwi_port+"/health"

values_list = []

while True:
    r = requests.get(url=health_url)
    
    current_health = r.json()['avgLoad']
    values_list.append(float(current_health))
    if len(values_list) > 10:
        values_list = values_list[1:]

    print(values_list)


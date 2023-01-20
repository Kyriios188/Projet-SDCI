import requests
from time import sleep

from flask import Flask

webapp = Flask(__name__)

url = "http://172.17.0.5:8181"


@webapp.route('/report')
def report():
   
   mean_health = sum(health_values_list)/10
   mean_latency = sum(latency_values_list)/10
   
   response = {
      'health': str(mean_health),
      'latency': str(mean_latency)
   }
   return(str(response))


@webapp.route('/monitor')
def monitor():
   global latency_values_list, health_values_list

   health_url = url + "/health"
   latency_url = url + "/ping"
   while True:
      # Monitor health
      r = requests.get(url=health_url)
      current_health = r.json()['avgLoad']
      health_values_list.append(float(current_health))
      if len(health_values_list) > 10:
         health_values_list = health_values_list[1:]

      print("HEALTH: "+str(health_values_list))

      r = requests.get(url=latency_url)
    
      current_latency = r.json()['pong']
      latency_values_list.append(int(current_latency))
      if len(latency_values_list) > 10:
         latency_values_list = latency_values_list[1:]

      print("LATENCY: "+str(latency_values_list))

      sleep(1)


if __name__ == '__main__':
   global latency_values_list, health_values_list
   latency_values_list = []
   health_values_list = []

   webapp.run(
      debug=True,
      host='0.0.0.0',
      port=5001
   )




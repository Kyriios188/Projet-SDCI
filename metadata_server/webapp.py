import json
import uuid
import requests
import os
from flask import Flask, request

webapp = Flask(__name__)


@webapp.route('/srv')
def srv():
   with open('metadata.json', 'r') as j:
      metadata = json.loads(j.read())
   
   return(str(metadata['srv']))

@webapp.route('/gwi')
def gwi():
   with open('metadata.json', 'r') as j:
      metadata = json.loads(j.read())
   
   return(str(metadata['gwi']))

@webapp.route('/gwf1')
def gwf1():
   with open('metadata.json', 'r') as j:
      metadata = json.loads(j.read())
   
   return(str(metadata['gwf1']))

@webapp.route('/gwf2')
def gwf2():
   with open('metadata.json', 'r') as j:
      metadata = json.loads(j.read())
   
   return(str(metadata['gwf2']))

@webapp.route('/gwf3')
def gwf3():
   with open('metadata.json', 'r') as j:
      metadata = json.loads(j.read())
   
   return(str(metadata['gwf3']))

@webapp.route('/dev1')
def dev1():
   with open('metadata.json', 'r') as j:
      metadata = json.loads(j.read())
   
   return(str(metadata['dev1']))

@webapp.route('/dev2')
def dev2():
   with open('metadata.json', 'r') as j:
      metadata = json.loads(j.read())
   
   return(str(metadata['dev2']))

@webapp.route('/dev3')
def dev3():
   with open('metadata.json', 'r') as j:
      metadata = json.loads(j.read())
   
   return(str(metadata['dev3']))

@webapp.route('/app')
def app():
   with open('metadata.json', 'r') as j:
      metadata = json.loads(j.read())
   
   return(str(metadata['app']))

@webapp.route('/ip', methods=['GET'])
def ip():
   ct_type: str = request.args.get('ct_type', type=str)
   reported_ip: str = request.args.get('ip', type=str)
   
   filename = 'metadata.json'
   with open(filename, 'r') as f:
      metadata = json.load(f)
      
      # Change the container's local ip value, though it's useless
      metadata[ct_type]["local_ip"] = reported_ip
      
      # Change the remote_ip value of the child containers
      if ct_type == "srv":
         metadata["gwi"]["remote_ip"] = reported_ip
      elif ct_type == "gwi":
         metadata["gwf1"]["remote_ip"] = reported_ip
         metadata["gwf2"]["remote_ip"] = reported_ip
         metadata["gwf3"]["remote_ip"] = reported_ip
      elif ct_type == "gwf1":
         metadata["dev1"]["remote_ip"] = reported_ip
      elif ct_type == "gwf2":
         metadata["dev2"]["remote_ip"] = reported_ip
      elif ct_type == "gwf3":
         metadata["dev3"]["remote_ip"] = reported_ip
   
   # create randomly named temporary file to avoid 
   # interference with other thread/asynchronous request
   tempfile = os.path.join(os.path.dirname(filename), str(uuid.uuid4()))
   with open(tempfile, 'w') as f:
      json.dump(metadata, f, indent=2)

   # rename temporary file replacing old file
   os.replace(tempfile, filename)
   
   return "200", 200


if __name__ == '__main__':
   webapp.run(
      debug=True,
      host='0.0.0.0',
      port=5000
   )
        


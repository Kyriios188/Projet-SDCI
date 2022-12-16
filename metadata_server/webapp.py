import json
import uuid
import os
from flask import Flask, request

webapp = Flask(__name__)


@webapp.route('/metadata/<str:ct_type>')
def metadata(ct_type: str):
   with open('metadata.json', 'r') as j:
      metadata = json.loads(j.read())
   
   return(str(metadata[ct_type]))


@webapp.route('/ip', methods=['GET'])
def ip():
   ct_type: str = request.args.get('ct_type', type=str)
   reported_ip: str = request.args.get('ip', type=str)
   
   filename = 'metadata.json'
   with open(filename, 'r') as f:
      metadata = json.load(f)
      
      # Change the container's local ip value
      # It's more logical to check a ct's ip using the metadata[ct][local_ip]
      # compared to a child's remote_ip value.
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
        


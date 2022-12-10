import json
from flask import Flask

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


if __name__ == '__main__':
   webapp.run(
      debug=True,
      host='0.0.0.0',
      port=5000
   )
        


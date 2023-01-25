import json
from flask import Flask

webapp = Flask(__name__)


@webapp.route('/metadata/<ct_type>')
def metadata(ct_type: str):
   with open('metadata.json', 'r') as j:
      metadata = json.loads(j.read())
   
   return(str(metadata[ct_type]))


if __name__ == '__main__':
   webapp.run(
      debug=True,
      host='0.0.0.0',
      port=5000
   )
        


import json
import uuid
import os
from flask import Flask, request

import health_monitoring_loop
import latency_monitoring_loop

webapp = Flask(__name__)


@webapp.route('/report')
def metadata(ct_type: str):
   response = {
      'health': str(health_monitoring_loop.values_list),
      'latency': str(latency_monitoring_lop.values_list)
   }
   return(str(reponse))


if __name__ == '__main__':
   webapp.run(
      debug=True,
      host='0.0.0.0',
      port=5001
   )
        


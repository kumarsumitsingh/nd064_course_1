import json
import logging
from flask import Flask
app = Flask(__name__)

@app.route("/")

def hello():
    app.logger.info("Main request successfull")
    return ("Hello World")

@app.route('/status')


def status():
    response=app.response_class(
        response=json.dumps({"result":"OK - healthy"}),
          status=200,
          mimetype='application/json')
    return response
@app.route('/metric')
def metric():
    response = app.response_class(
          response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
          status=200,
          mimetype='application/json'
          )
    return response



if __name__ == "__main__":
     #Stream logs to a file, and set the default log level to DEBUG
    #logging.basicConfig(filename='app.log',level=logging.DEBUG)
    logging.basicConfig(level=logging.DEBUG,filename='myapp.log',force='true')
    logging.info('This is a info')
    app.run(host='0.0.0.0')

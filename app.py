from flask import Flask, jsonify, request

import json
from slack import performSlackAction

application = Flask(__name__)


@application.route('/')
def hello_world():
    info = {"Text" : "Hi"}
    return jsonify(info)

# Route for Slack Apps
@application.route('/slack/apps/<appName>/<command>', methods=["GET", 'POST'])
def query_slack_app(appName, command):
    return jsonify(performSlackAction(appName, command, [ "None" ]))
    
    
if __name__ == '__main__':
    application.run(debug=True, host='0.0.0.0', port=8000)

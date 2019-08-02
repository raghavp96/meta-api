from flask import Flask, jsonify, request

import json
from slack import performSlackAction

app = Flask(__name__)


@app.route('/')
def hello_world():
    info = {"Text" : "Hi"}
    return jsonify(info)

# Route for Slack Apps
@app.route('/slack/apps/<appName>/<command>', methods=["GET", 'POST'])
def query_slack_app(appName, command):
    return jsonify(performSlackAction(appName, command, [ "None" ]))
    
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)

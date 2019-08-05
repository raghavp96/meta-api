from flask import Flask, jsonify, request

import json
from slack import performSlackAction

application = Flask(__name__)


@application.route('/')
def hello_world():
    info = {"Text" : "Hi"}
    return jsonify(info)


# Route for Slack Apps
@application.route('/slack/apps/<appName>/<command>', methods=['GET', 'POST'])
def query_slack_app(appName, command):
    if request.method == 'GET':
        return jsonify({ "Text" : "Hit this endpoint with a POST request instead to actually do something" })
    if request.is_json:
        return jsonify(performSlackAction(appName, command, request.get_json(force=True)))
    else:
        return jsonify(performSlackAction(appName, command, request.form))
 
    
if __name__ == '__main__':
    application.run(debug=True, host='0.0.0.0', port=8000)

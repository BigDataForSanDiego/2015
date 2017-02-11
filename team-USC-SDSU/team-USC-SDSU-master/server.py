import os
from flask import Flask, request, jsonify
import twilio.twiml
from twitter import *

app = Flask(__name__)
app.config.from_object(__name__)

CONSUMER_KEY = 'Some Key'
CONSUMER_SECRET = 'Shhh its a secret'
ACCESS_TOKEN = 'birdy coin'
ACCESS_TOKEN_SECRET = 'birdy secret coin'

t = Twitter(auth=OAuth(ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET))

@app.route('/')
def default_resp():
	return 'Welcome to default webpage!'

@app.route('/my_app', methods=['GET', 'POST'])
def my_app():

	get_body = request.values.get('Body')
	if len(get_body) <= 140:
		t.statuses.update(status=get_body)
	else:
		t.statuses.update(status=get_body[:140])

	resp = twilio.twiml.Response()
	resp.message(getCenters())
	return str(resp)

def getCenters():
        try:
                f = open('safety_centers.txt', 'r')
                read_file = f.read()
                f.close()
                return read_file
        except:
                return 'Error !'


port = os.getenv('VCAP_APP_PORT', 8000)

if __name__ == '__main__':
	app.debug = True
	app.run(host= '0.0.0.0', port=int(port))

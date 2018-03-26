from flask import Flask
from flask import make_response
import json

app =  Flask(__name__)

@app.route("/")
def hello():
	return "Test"

@app.route("/m/product")
def retrieve_product():
	sample_product = {
		'_key' : 'Maki',
		'name' : 'Maki Nishikino',
		'is_available' : True,
		'type' : 'food',
		'rating' : 4.0
	}
	resp = make_response(json.dumps(sample_product), 200)
	resp.headers['abeona-token'] = "63a51933-092b-46e1-8b14-45e250af2616"

	return resp

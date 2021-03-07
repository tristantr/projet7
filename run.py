from flask import Flask, render_template, request, jsonify
from grandpy.response import Response
import os
import logging 

app = Flask(__name__)

logger = logging.getLogger()

formatter = logging.Formatter('%(process)d %(asctime)s %(name)-12s %(levelname)-8s %(message)s')

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
logger.setLevel(logging.INFO)

logger.info(os.environ)



@app.route('/')
def index():
	return render_template('mainpage.html')

@app.route('/process/', methods=['POST'])
def process():
	data = request.get_json()
	question = data['question']
	response = Response(question).get_response()
	return response

if __name__ == "__main__":
    app.run(debug=True)	




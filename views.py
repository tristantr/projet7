from flask import Flask, render_template, request, jsonify
from grandpy.response import Response

app = Flask(__name__)

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




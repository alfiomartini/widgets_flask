from flask import Flask, request, json, jsonify
import requests
from flask_cors import CORS

from dotenv import load_dotenv
import os

app = Flask(__name__)
CORS(app)

# only for development
# load_dotenv('.env')

Y2B_URL = os.getenv('Y2B_URL')
Y2B_KEY = os.getenv('Y2B_KEY')

TRANS_URL = os.getenv('TRANS_URL')
TRANS_KEY = os.getenv('TRANS_KEY')

UNSPLASH_URL = os.getenv('UNSPLASH_URL')
UNSPLASH_KEY = os.getenv('UNSPLASH_KEY')


@app.route('/')
def index():
    # print(app.config)
    return jsonify('Hello Widgets Server')


@app.route('/youtube/<string:input>')
def youtube(input):
    url = f"{Y2B_URL}&key={Y2B_KEY}&q={input}"
    try:
        resp = requests.get(url)
        return resp.json()
    except:
        return jsonify('failure'), 400


# https://stackoverflow.com/questions/10999990/get-raw-post-body-in-python-flask-regardless-of-content-type-header
@app.route('/translate', methods=['POST'])
def translate():
    url = f"{TRANS_URL}"
    data = json.loads(request.data)
    print(data)
    try:
        resp = requests.post(
            url, data={'key': TRANS_KEY, 'q': data['input'], 'target': data['code']})
        return resp.json()
    except:
        print('hello exception')
        return jsonify("Failure"), 400


@app.route('/unsplash/<string:input>')
def unsplash(input):
    url = f"{UNSPLASH_URL}?query={input}&per_page=30"
    headers = {'Authorization': f"Client-ID {UNSPLASH_KEY}"}
    try:
        resp = requests.get(url, headers=headers)
        return resp.json()
    except:
        print('Hello Exception')
        return jsonify('failure'), 400


if __name__ == '__main__':
    app.run(debug=True)

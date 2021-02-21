from flask import Flask, request, json, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

Y2B_URL = 'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&type=video'
Y2B_KEY = 'AIzaSyCvrvgwxxdGsNiTKExH1UEGvs5rKLb8r3Q'

TRANS_URL = 'https://translation.googleapis.com/language/translate/v2'
TRANS_KEY = 'AIzaSyDyPQSJqbpyOUpKffETJNUi7q6Fq6G8RsA'

UNSPLASH_URL = 'https://api.unsplash.com/search/photos'
UNSPLASH_KEY = '_KsPY_y0zTjR3q1mW2-BU29AXbX8FqZ171JBmkXJrRw'


@app.route('/')
def index():
    return '<h1> Hello World </h1>'


@app.route('/youtube/<string:input>')
def youtube(input):
    url = f"{Y2B_URL}&key={Y2B_KEY}&q={input}"
    resp = requests.get(url)
    print(resp.status_code)
    return resp.json()


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

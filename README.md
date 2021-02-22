# A Flask Server for Widgets Collection

This is a small server written in Flask for the widgets application. This was needed in order to avoid exposing private keys used to access the resources of the severall apps inside the application. The server is comprised of three endpoints:

- GET /youtube/{_subject_}: return a JSON list of videos about subject

`curl https://widgets-flask.herokuapp.com/youtube/NicoleCross`

- GET /unsplash/{_subject_}: return a JSON list of images related to subject

`curl https://widgets-flask.herokuapp.com/unsplash/libraries`

- POST /translate : return JSON data with source text translated to target language

`curl -X POST -H "Content-Type: application/json" -d '{"input":"Hello World", "code":"pt"}' https://widgets-flask.herokuapp.com/translate`

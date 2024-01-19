from flask import Flask, request
import requests
import os
from requests.auth import HTTPBasicAuth

app = Flask(__name__, static_url_path="")

@app.route('/')
def index():
    f = open("tracksByYears.html", "r")
    page = f.read()
    f.close()
    return page

@app.route('/songs', methods=["POST"])
def showSongs():
    form = request.form
    year = form["year"]
    f = open("tracksByYears.html", "r")
    page = f.read()
    f.close()
    clientID = os.environ['CLIENT_ID']
    clientSecret = os.environ['CLIENT_SECRET']

    url = "https://accounts.spotify.com/api/token"
    data = {"grant_type": "client_credentials"}
    auth = HTTPBasicAuth(clientID, clientSecret)

    response = requests.post(url, data=data, auth=auth)
    accessToken = response.json()["access_token"]

    url = "https://api.spotify.com/v1/search"
    headers = {'Authorization': f'Bearer {accessToken}'}
    search = f"?q=year%3A{year}&type=track&limit=10"
    fullURL = f"{url}{search}"

    response = requests.get(fullURL, headers=headers)
    data = response.json()

    
    tracks_html = ""
    for track in data['tracks']['items']:
        track_name = track['name']
        preview_url = track['preview_url']
        track_html = f'<p>{track_name}</p><audio controls><source src="{preview_url}" type="audio/mpeg"></audio><hr>'
        tracks_html += track_html

    page = page.replace("{title}", tracks_html)
    return page

app.run(host='0.0.0.0', port=81)

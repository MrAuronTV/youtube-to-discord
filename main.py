#!/usr/bin/env python3
import pickle
import requests
import json
from urllib import request
from urllib.error import HTTPError
from json import loads
import urllib.request

WEBHOOK_URL = 'YOUR_WEBHOOK_URL' # Discord webhook url
PATH = 'YOUR_PATH' #Path where you stock clip id for doesnt spam discord

try:
    id = pickle.load(open("{}/lastvideo".format(PATH), "rb"))
except (OSError, IOError) as e:
    foo = 3
    pickle.dump(foo, open("{}/lastvideo".format(PATH), "wb"))


API_ENDPOINT = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId=<PLAYLIST ID>&key=<YOUTUBE API TOKEN>&maxResults=1'

#api call here
r = requests.get(url = API_ENDPOINT)

TITLE = loads(r.text)['items'][0]['snippet']['title'] # title video
VIDEO = loads(r.text)['items'][0]['snippet']['resourceId']['videoId'] # id video
URL = "https://i.ytimg.com/vi/{}/mqdefault.jpg".format(VIDEO) # thumbnails
DATE = loads(r.text)['items'][0]['snippet']['publishedAt'] # date

# La payload
payload = {
    'username':"bot username",
    'content': "content message",
    'avatar_url':"bot avatar",
    'embeds': [
        {
            'title': TITLE, 
            'description': 'description',  
            'url': 'https://www.youtube.com/watch?v={}'.format(VIDEO),  
            "color": 16711680,
	    'author': {'name': 'author'}, 
            'timestamp': DATE,
            "image": {"url": URL}, 
        },
    ]
}

# header parameters
headers = {
    'Content-Type': 'application/json',
    'user-agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'
}

# request discord
req = request.Request(url=WEBHOOK_URL,
                      data=json.dumps(payload).encode('utf-8'),
                      headers=headers,
                      method='POST')

if VIDEO:
    if VIDEO != id :
       response = request.urlopen(req)
with open('{}/lastvideo'.format(PATH), 'wb') as f:
    pickle.dump(VIDEO, f)

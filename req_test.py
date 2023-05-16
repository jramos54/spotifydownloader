import requests
import json
from bs4 import BeautifulSoup

#response=requests.get('https://open.spotify.com/album/1Xc3NrUQWfWlJz6kVNKpq1?si=HxCAihDHQMGLqVsTkF8iWQ')
response=requests.get('https://open.spotify.com/album/4ihlEk0yuvUpKGSX8A9ITz')
response_html=BeautifulSoup(response.text,'html.parser')

print(response.status_code)
title=str(response_html.title.string)
title=title[:title.index('-')].strip()

tracks=response_html.find_all(draggable="false")

for track in tracks:
    if track.name == 'a':
        if track.get('href').startswith('/artist'):
            continue
        else:
            print(track.get('href'))
            print(track.text)
    





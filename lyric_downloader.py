# -*- coding: utf-8 -*-
import requests, json
from bs4 import BeautifulSoup



base_url = "https://api.genius.com"
client_access_token = "8vVt8TPGXXSztJ52FhidJiVCSt56XyAaaywPBfNOmxp1_UB7ZHIDpfXyu6vrZt0n"
headers = {'Authorization': 'Bearer TOKEN'}
artist_name = ""

def _get(path, params=None, headers=None):
    
    query = '/'.join([base_url, path])
    token = "Bearer {}".format(client_access_token)
    
    if headers:
        headers['Authorization'] = token
    else:
        headers = {'Authorization': token}
        
    response = requests.get(url=query, params=params, headers=headers)
    response.raise_for_status()
    
    return response.json()
                            
                            
                            
def get_songs(artist_id):
    # variables and list
    current_page = 1
    next_page = True
    songs = []
    
    while next_page:
        path = "artists/{}/songs/".format(artist_id)
        params = {'page': current_page}
        data = _get(path=path, params=params)
        
        page_songs = data['response']['songs']
        
        if page_songs:
            # add all songs on current page, loop onto next page
            songs += page_songs
            current_page += 1
            print("querying from page " + str(current_page))
        else:
            next_page = False
    
    song_ids = [song["id"] for song in songs
             if song["primary_artist"]["id"] == artist_id]
    
    return song_ids

def get_lyrics(song_ids, artist_id):
    
    lyrics_dict = {}
    
    
    for i, song_id in enumerate(song_ids):
       # song = str(song)
       
       song_id = str(song_id)
       song_url = _get(path=song_id)
       response = requests.get(song_url, headers=headers)
       json = response.json()
       print(json)
       #song_path = json["response"]["song"]["path"]
       page_url = "http://genius.com" + str(json)
       page = requests.get(page_url)
       html = BeautifulSoup(page.text, "html.parser")
       [h.extract() for h in html('script')]
        
       lyrics = html.find("div", class_="lyrics").get_text()
        
       lyrics_dict[song] = lyrics 
        
    return lyrics
    
get_lyrics(song_ids, 72)


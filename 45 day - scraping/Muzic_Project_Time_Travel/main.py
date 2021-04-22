import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

url = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(url)
data = response.text

soup = BeautifulSoup(data, features="html.parser")

titles = [title.getText() for title in soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")]


client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
print(client_id)
print(client_secret)


sp = spotipy.Spotify(           # authentication
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id= client_id,
        client_secret= client_secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]

for song in titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")  # search the song in spotify
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False) # create your playlist

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
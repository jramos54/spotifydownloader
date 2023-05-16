# from savify import Savify
import subprocess
from subprocess import Popen
CLIENT='e09ffe6d4b22485b84e5d9fa9565f189'
SECRET='e35e812c02e540329ac427ca143fd569'
# link='https://open.spotify.com/track/0zG79kNUroO9ZQtuV67gPt'


# s = Savify(api_credentials=(CLIENT,SECRET))

# s.download(link, '--no-check-certificate')


import spotdl
from spotipy.oauth2 import SpotifyClientCredentials

# Credenciales de la aplicación de Spotify
client_id = CLIENT
client_secret = SECRET

# Crea una instancia de la clase SpotifyClientCredentials para autenticarte en la API de Spotify
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
#spotdl.spotdl.SpotifyAPI.set_credentials_manager(client_credentials_manager)

# Definir la URL de la canción de Spotify que se desea descargar
song_url = "https://open.spotify.com/track/1dGr1c8CrMLDpV6mPbImSI"

#commands=['cd I:\\potifydownload\\test\\',f'spotdl download {song_url}']
# Descargar la canción utilizando SpotDL
#subprocess.run(,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
#spotdl.download_song(song_url)
#processes = [Popen(cmd, shell=True) for cmd in commands]
subprocess.call(f'spotdl download {song_url}',cwd='I:\\potifydownload\\test\\')
#print(processes)
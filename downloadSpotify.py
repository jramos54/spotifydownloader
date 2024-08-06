import os
from savify.utils import PathHolder
from savify import Savify,logger
import logging
import requests
from bs4 import BeautifulSoup

links=[]
files=[]

# Accesos de Spotify
CLIENT='e09ffe6d4b22485b84e5d9fa9565f189'
SECRET='e35e812c02e540329ac427ca143fd569'

# Folders de la aplicacion
ROOT='F:\potifydownload\descargas'
EXECFOLDER='F:\potifydownload\descargas\_execution'

# Link de spotify
LINKROOT='https://open.spotify.com'

# Se crea el logger
log_dir=logger.Logger(log_location=EXECFOLDER,log_level=logging.info(1))

# Listar los directorios
directories=os.listdir(ROOT)

# extraer los directorios destino y el archivo de los links
for directory in directories:
    if os.path.isdir(ROOT+'\\'+directory):
        base_dir=ROOT+'\\'+directory+'\\'

        if base_dir != EXECFOLDER+'\\':
            dir_files=[(base_dir,base_dir+x) for x in os.listdir(base_dir)]
            files.extend(dir_files)

# Leer los links de cada uno de los archivos       
for file in files:
    parendirectory,openfile=file
    if "_execution" in parendirectory:
        continue
    print(f'{openfile}\n{parendirectory}')
    with open(openfile) as f:

# Se listan los links que hay en el archivo
        links=[line for line in f]
        for link in links:

# Se extrae el titulo del album de cada link            
            response=requests.get(link)
            response_html=BeautifulSoup(response.text,'html.parser')
            title=str(response_html.title.string)
            title=title[:title.index('-')].strip()
            print(f"album:\n{title}")
            print(link)

# Se extraen los links de cada una de las canciones
            tracks=response_html.find_all(draggable="false")

            for track in tracks:
                if track.name == 'a':

# Se crea el folder del album y los links de cada uno de las canciones
                    if not track.get('href').startswith('/artist'):
                        link_track=LINKROOT+track.get('href')
                        album_directory=parendirectory+'\\'+title
                        if not os.path.exists(album_directory):
                            os.makedirs(album_directory)

# Se descargan las canciones individuales
                        path_holder=PathHolder(data_path=EXECFOLDER,downloads_path=album_directory)
                        print(f"cancion: {track.text}")
                        print(link_track)
                        
                       
                        s = Savify(api_credentials=(CLIENT,SECRET),path_holder=path_holder,logger=log_dir)
                        s.download(link_track,'--no-check-certificate')
                        

###################################################################
#             ruta=f"spotify_dl -V -l {link[:-2]} -o {parendirectory}"
#             print(ruta+'\n')
#             os.system(ruta)

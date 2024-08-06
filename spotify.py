import os
import subprocess
import logging
import requests
from bs4 import BeautifulSoup
from scrappping import get_links

# Accesos de Spotify
CLIENT = 'e09ffe6d4b22485b84e5d9fa9565f189'
SECRET = 'e35e812c02e540329ac427ca143fd569'

# Directorios de la aplicación
ROOT = 'F:\\potifydownload\\descargas'
EXECFOLDER = 'F:\\potifydownload\\descargas\\_execution'
LINKROOT = 'https://open.spotify.com'

# Configuración del logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Crear un handler para el archivo
file_handler = logging.FileHandler(filename=os.path.join(EXECFOLDER, 'log.txt'), encoding='utf-8', mode='w')
file_handler.setLevel(logging.INFO)

# Crear un handler para la consola
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Crear un formato y agregarlo a los handlers
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Agregar los handlers al logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Lista de directorios dentro de ROOT
directories = os.listdir(ROOT)

# Funciones para ejecutar spotify_dl
def set_environment_variables():
    os.environ['SPOTIPY_CLIENT_ID'] = CLIENT
    os.environ['SPOTIPY_CLIENT_SECRET'] = SECRET

def run_spotify_dl(song_link, album_directory):
    command = ['spotify_dl', '-l', song_link, '-o', album_directory]
    logger.info(command)
    subprocess.run(command)

set_environment_variables()

# Procesar cada archivo en los directorios
for directory in directories:
    base_dir = os.path.join(ROOT, directory)
    logger.info(f"en directorio {base_dir}")

    if os.path.isdir(base_dir) and base_dir != EXECFOLDER:
        for filename in os.listdir(base_dir):
            file_path = os.path.join(base_dir, filename)

            if os.path.isfile(file_path):
                logger.info(f'Procesando archivo: {file_path}')
                try:
                    with open(file_path) as f:
                        links = [line.strip() for line in f if line.strip()]

                    for link in links:
                        response = requests.get(link)
                        response_html = BeautifulSoup(response.text, 'html.parser')
                        title = str(response_html.title.string.split('-')[0].strip())
                        logger.info(f"Álbum: {title}\nEnlace: {link}")

                        album_directory = os.path.join(base_dir, title)
                        if not os.path.exists(album_directory):
                            os.makedirs(album_directory)

                        # Extraer los enlaces de cada una de las canciones
                        
                        tracks = get_links(link)
                        
                        for track in tracks:
                            logger.info(f" {type(track)} - {track}")
                            if track.get('href') and not track.get('href').startswith('/artist'):
                                song_link = LINKROOT + track.get('href')
                                logger.info(f"Descargando canción: {song_link}")
                                run_spotify_dl(song_link, album_directory)
                except PermissionError as e:
                    logger.error(f"Error de permiso al abrir {file_path}: {e}")
                except Exception as e:
                    logger.error(f"Error al procesar {file_path}: {e}")
            else:
                logger.info(f"Omitido: {file_path} no es un archivo")

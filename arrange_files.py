import os
import shutil

def sort_artist(ruta_base):
    # Asegurarnos de que la ruta base existe
    if not os.path.exists(ruta_base):
        print(f"La ruta {ruta_base} no existe.")
        return
    
    for raiz, directorios, archivos in os.walk(ruta_base):
        for archivo in archivos:
            nombre_partes = archivo.split('-')
            
            # Verificamos que el archivo tenga al menos tres partes
            if len(nombre_partes) < 3 or not archivo.lower().endswith('.mp3'):
                continue
            
            artista = nombre_partes[1]
            nueva_ruta = os.path.join(ruta_base, artista)
            
            # Crear la carpeta del artista si no existe
            if not os.path.exists(nueva_ruta):
                os.makedirs(nueva_ruta)
            
            ruta_origen = os.path.join(raiz, archivo)
            ruta_destino = os.path.join(nueva_ruta, archivo)
            
            # Mover el archivo a la nueva carpeta
            try:
                shutil.move(ruta_origen, ruta_destino)
                # print(f"Movido: {ruta_origen} -> {ruta_destino}")
            except Exception as e:
                print(f"Error al mover {ruta_origen} a {ruta_destino}: {e}")

def listar_directorios(ruta_base):
    if not os.path.exists(ruta_base):
        print(f"La ruta {ruta_base} no existe.")
        return []
    
    directorios = [os.path.join(ruta_base, nombre) for nombre in os.listdir(ruta_base) if os.path.isdir(os.path.join(ruta_base, nombre))]
    
    return directorios

def run_sorting(ruta_base):
    
    # rutas_base = [
    #     r'F:\MUSICA\Musica\BandayNorteña',
    #     r'F:\MUSICA\Musica\BoleroyFolclorica',
    #     r'F:\MUSICA\Musica\Rockypop',
    #     r'F:\MUSICA\Musica\SalsayCumbia',
    #     r'F:\MUSICA\Musica\TrovayBalada'
    # ]

    rutas_base=listar_directorios(ruta_base)
    for _ in rutas_base:
        sort_artist(_)

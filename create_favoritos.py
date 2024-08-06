import os
import shutil

def create_folder(carpeta):
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

def move_favorites(ruta_archivo, favoritos_base, archivo):
    partes = archivo.rsplit('-', 2)  # Dividir desde el final solo en 3 partes máximo
    if len(partes) < 3:
        print(f"El archivo {archivo} no cumple con el formato esperado.")
        return
    
    title, artist, album = partes
    album = album.rstrip('.mp3').rstrip('.MP3')  # Remover extensión si está en mayúscula
    
    subcarpeta = artist
    nueva_ruta = os.path.join(favoritos_base, subcarpeta)
    create_folder(nueva_ruta)
    
    nuevo_nombre = f"{title}-{artist}-{album}.mp3"
    ruta_destino = os.path.join(nueva_ruta, nuevo_nombre)
    
    # Si el archivo ya existe en el destino, renombrar el archivo
    if os.path.exists(ruta_destino):
        base, extension = os.path.splitext(ruta_destino)
        contador = 1
        while os.path.exists(ruta_destino):
            ruta_destino = f"{base}_{contador}{extension}"
            contador += 1
    
    try:
        shutil.move(ruta_archivo, ruta_destino)
        # print(f"Movido: {ruta_archivo} -> {ruta_destino}")
        return ruta_destino
    except Exception as e:
        print(f"Error al mover {ruta_archivo} a {ruta_destino}: {e}")
        return None

def create_list(lista_m3u8, ruta_base, favoritos_base):
    # Crear la carpeta favoritos si no existe
    create_folder(favoritos_base)
    
    if not os.path.exists(lista_m3u8):
        print(f"El archivo {lista_m3u8} no existe.")
        return
    
    nuevas_lineas = []
    
    with open(lista_m3u8, 'r', encoding='utf-8') as file:
        lineas = file.readlines()
    
    for linea in lineas:
        linea = linea.strip()
        if linea.startswith('#') or not linea.endswith('.mp3'):
            nuevas_lineas.append(linea)
            continue
        
        archivo = os.path.basename(linea)
        
        # Buscar el archivo en todos los subdirectorios
        found = False
        for raiz, directorios, archivos in os.walk(ruta_base):
            if archivo in archivos:
                ruta_completa = os.path.join(raiz, archivo)
                ruta_destino = move_favorites(ruta_completa, favoritos_base, archivo)
                if ruta_destino:
                    # Convertir la ruta absoluta en ruta relativa a favoritos_base
                    ruta_relativa = os.path.relpath(ruta_destino, favoritos_base)
                    ruta_relativa = ruta_relativa.replace('/', '\\')
                    nuevas_lineas.append(f"favoritas\\{ruta_relativa}")
                found = True
                break
        
        if not found:
            print(f"Archivo no encontrado: {archivo}")
            nuevas_lineas.append(linea)
    
    # Sobrescribir el archivo .m3u8 con las nuevas líneas
    with open(lista_m3u8, 'w', encoding='utf-8') as file:
        for nueva_linea in nuevas_lineas:
            file.write(nueva_linea + '\n')

def run_favorites(ruta_base):
    favoritos_base = os.path.join(ruta_base, 'favoritas')
    lista_m3u8 = os.path.join(ruta_base, 'favoritas.m3u8')

    print(f"Usando lista de favoritos: {lista_m3u8}")
    create_list(lista_m3u8, ruta_base, favoritos_base)

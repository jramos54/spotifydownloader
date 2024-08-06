import os
import re

def files_dont_match(ruta_base):
    patron_directorio_principal = re.compile(r'^#.+$')
    patron_archivo = re.compile(r'^[^-]+-.+-[^-]+\.mp3$')
    
    archivos_no_cumplen = []
    
    for raiz, directorios, archivos in os.walk(ruta_base):
        partes_ruta = raiz.split(os.sep)
        
        # Verificar si estamos en una carpeta principal que empieza con #
        if len(partes_ruta) > 1 and not patron_directorio_principal.match(partes_ruta[1]):
            continue
        
        for archivo in archivos:
            ruta_completa = os.path.join(raiz, archivo)
            partes = ruta_completa.split(os.sep)
            
            if len(partes) < 3:
                archivos_no_cumplen.append(ruta_completa)
                continue
            
            directorio_principal = partes[-3]
            subdirectorio = partes[-2]
            nombre_archivo = partes[-1]
            
            if not patron_directorio_principal.match(directorio_principal):
                archivos_no_cumplen.append(ruta_completa)
                continue
            
            nombre_partes = nombre_archivo.split('-')
            if len(nombre_partes) < 3:
                archivos_no_cumplen.append(ruta_completa)
                continue
            
            nombre_esperado = f'{nombre_partes[0]}-{directorio_principal[1:]}-{subdirectorio}.mp3'
            if not patron_archivo.match(nombre_archivo) or nombre_esperado != nombre_archivo:
                archivos_no_cumplen.append(ruta_completa)
    
    return archivos_no_cumplen


def run_matching_files(ruta_base):
    # ruta_base = 'G:\\MUSICA'
    archivos_no_cumplen = files_dont_match(ruta_base)

    if archivos_no_cumplen:
        print("Archivos que no cumplen con el patrón:")
        for archivo in archivos_no_cumplen:
            print(archivo)
        print(f"\nTotal de archivos que no cumplen: {len(archivos_no_cumplen)}")
    else:
        print("Todos los archivos cumplen con el patrón.")

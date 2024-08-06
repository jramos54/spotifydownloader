import pyperclip as pc
import os
import sys

def create_or_append_to_file(target, links):
    dir_path = f'F:\\potifydownload\\descargas\\{target}'
    if not os.path.exists(dir_path):
        try:
            os.makedirs(dir_path)
        except OSError as e:
            print(f"Error al crear el directorio: {e.strerror}")
            return False
    file_path = os.path.join(dir_path, f'{target}.txt')
    with open(file_path, 'a') as f:
        for link in links:
            f.write(link)
    return True

if __name__ == "__main__":
    while True:
        target = input('Qué se copiará (espacios usar _ ) o escriba "exit" para salir:\t')
        if target.lower() == 'exit':
            sys.exit(0)

        target = target.replace(' ', '_')
        links = []
        while True:
            
            try:
                link = pc.waitForNewPaste(timeout=30)
                links.append(link + '\n')
                print(f"{len(links)} link copiado:\n{link}\n")
            except:
                entrada = input('Presione cualquier tecla para continuar o "n" para un nuevo target:\t')
                if entrada.lower() == 'n':
                    break  # Salir del bucle interno para ingresar un nuevo target
                elif target.lower() == 'exit':
                    sys.exit(0)
        if create_or_append_to_file(target, links):
            print("Archivo Guardado Exitosamente")

import subprocess
import os

path = 'H:\\testDown'

for root,dirs,files in os.walk(path):
    print('---'*10,root,'---'*10)
    for file in files:
        if file[-3:]=='mp4':
            ruta='\"'+root+'\\'+file[:-4]+'\"'
            filename='\"'+root+'\\'+file[:-4]+'\"'
            cadena='ffmpeg -i '+ruta+'.mp4 '+filename+'.mp3'
            print(subprocess.run(cadena,shell=True))
            #print(cadena)
'''
print(subprocess.run('ffmpeg -i "H:\\testDown\\Canta Con Banda\\Francisco #Charro# Avitia - China de los Ojos Negros".webm "filename".mp3',shell=True,capture_output=True))
'''
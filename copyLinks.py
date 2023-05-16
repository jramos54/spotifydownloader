import pyperclip as pc
import os
import time
import sys

target=input('Que se copiara (espacios usar _ )?:\t')

var=True
links=[]

while var:
    try:
        link=pc.waitForNewPaste(timeout=30)
        links.append(link+'\n')
        print(f"{len(links)} link copiado:\n{link}\n")
    except:
        entrada=input('continuar y/n?:\t')
        if entrada.lower()!='n':
            continue
        else:
            var=False
        
os.mkdir('I:\potifydownload\\descargas\\'+target)
parent_dir='I:\potifydownload\\descargas\\'+target+'\\'+target+'.txt'

with open(parent_dir,'a') as f:
    for link in links:
        f.write(link)
 
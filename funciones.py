import os.path as path
import json

def exists():
    if path.exists('data.final'):
        return True
    else:
        with open('data.final', 'w+', encoding="latin1") as file: 
            a = ['Contenido: ']
            f = ''
            for line in a:
                f = f + line
            file.write(f)
            file.close()
    return True



def agregar(a):
    if exists():
        with open('data.final', 'r+', encoding="latin1") as file: 
            l = file.read()
            l = str(l)
            l = l.split('\n')
            temp = str('\n '+a)
            print(temp)
            l.append(temp)
            f = ''
            print(l)
            for line in l:
                f = f + line
            file.write(f)
            file.close()



def leer():
    if exists():
        with open('data.final','r+', encoding="latin1") as file:
            l = file.read()
            l = l
            l = str(l)
            return l
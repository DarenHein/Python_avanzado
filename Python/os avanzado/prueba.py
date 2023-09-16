
#todo vamos a hacer una prueba recorrer un escritorio anidado 

import os 
import zipfile 

try : 
    nombre = "compri.zip"
    ruta = os.getcwd()
    existe = os.path.exists(ruta)
    compri = zipfile.ZipFile(nombre,"w")
    lista = []
    if existe : 
        print("ruta existe en el sistema ")
        for directorio , sub , archivo in os.walk(ruta):
            print(directorio)
            print(sub)
            print(archivo)
            lista.append(archivo)
            print("\n")
        print(lista)
        nombre = lista[0][0]
        ruta_abs  = os.path.abspath(nombre)
        print(ruta_abs)
    else : 
        print("ruta no existe en el sistema")
    pass
except OSError : 
    print("Error en modulo os ")
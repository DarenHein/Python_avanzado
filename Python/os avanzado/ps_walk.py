
#todo ejemplo de os walk lo estudio por que ayudara en la creacion de proyect_cat
#tpdp que hace os walk os walk nos permite abrir direcotiors dentro de dictorios ejemplo 
'''
+directorio 
    ° hola.txt
    ° direcotrio 
        °hola.txt
        direcotrio2 
            °hola3.txt
'''
import os

try : 
    ruta = os.getcwd()
    for directorio , subdirectorios , archivos in os.walk(ruta):
        print(directorio)
        print(subdirectorios)
        print(archivos)
        print("\n")
    pass 
except OSError : 
    print("Error en modulo os")


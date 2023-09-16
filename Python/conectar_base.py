
#todo en este apartado veremos como conectar una base de datos a python 
import mysql.connector
nombre = "root" #nombre del propietario de la base de datos 
contra = "58825613"
host= "localhost"
base_datos = "llaves"

try : 
    conexion = mysql.connector.connect(
        user = nombre,
        password = contra , 
        host = host , 
        database = base_datos
    )
    if conexion.connect : 
        print("Base de datos conectada con exito ")
    else : 
        print("BAse de datos no conectada")
    pass
except mysql.connector.Error: 
    print("Error en el momento de conectar")
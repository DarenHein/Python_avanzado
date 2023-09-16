
#todo objeto cursor 
import mysql.connector

nombre = "root"
contra = "58825613"
host = "localhost"
base = "llaves"

try : 
    conexion = mysql.connector.connect(
        user = nombre ,
        password = contra,
        host = host,
        database = base 
    )
    if conexion.connect: 
        print("Base de datos conectada con exito ")
        #todo LOS OBJETOS CURSORES NOS AYUDAN A HACER CONSULTAS ALAS BASES DE DATOS 
        cursor = conexion.cursor() #todo objeto cursor creado 
        cursor.close() #todo siempre cerrar cursor 
        conexion.close() #todo tambien cerrar la base de datos 
    else : 
        print("La base de datos no se pudo conectar")
    pass 
except mysql.connector.Error: 
    print("Bade de datos no conectadad ")
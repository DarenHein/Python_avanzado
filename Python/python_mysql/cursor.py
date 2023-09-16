import mysql.connector
#todo cursor 
#todo execute -> realiza un query en mysql 
#todo fetchall -> decuelve el query realizado en tupla 
#todo fetchone -> devuelve el query realizado en lista 
try :
    nombre = "root"
    contra = "58825613" 
    host = "localhost"
    base = "liberia"
    conexion = mysql.connector.connect(
        user = nombre,
        password = contra,
        host = host,
        database = base 
    )
    if conexion.connect: 
        print("base de datos conectada con exito")
        cursor = conexion.cursor() 
        cursor.execute("select * from autor;")#todo se ocupa para crear querys con mysql
        resultados = cursor.fetchall() #todo fetchall devuelve todos los resultados del query que se realiza con execute pero en tupla 
        for elementos in resultados: #todo como sin tuplas pcuapmos un for para recorrer el dato 
            print(elementos)
    else : 
        print("Conexion invalida")
    pass 
except mysql.connector.Error: 
    print("Error encontrado en el modulo mysql")



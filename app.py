import psycopg2

connection = psycopg2.connect(
    host = "localhost",
    user = "postgres",
    password = "Vicky120600*",
    database = "test",
    port = "5432"
)

connection.autocommit = True

def crear_tabla():
    cursor = connection.cursor()
    query = "CREATE TABLE usuario(nombre varchar(30),email varchar(30),telefono varchar(11))"
    try:
        cursor.execute(query)
    except:
        print("La tabla ya existe")
    cursor.close()

def insertar_datos():
    cursor = connection.cursor()
    query = """ INSERT INTO usuario (nombre,email,telefono) values ('Emmanuel','emma@gmail.com','3124')"""
    cursor.execute(query)
    cursor.close()
    
def actualizar_datos():
    cursor = connection.cursor()
    query = """ UPDATE usuario set nombre = 'Felipe' WHERE nombre = 'Emmanuel' """
    cursor.execute(query)
    cursor.close()

def eliminar_tabla():
    cursor = connection.cursor()
    query = "DROP TABLE usuario"
    cursor.execute(query)
    cursor.close()

# crear_tabla()
actualizar_datos()
# insertar_datos()
# eliminar_tabla()
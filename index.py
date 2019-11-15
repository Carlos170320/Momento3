import sqlite3

conexion = sqlite3.connect('ejemplo1.db')

# Creamos el cursor
cursor = conexion.cursor()

# Ahora crearemos una tabla de usuarios para almacenar nombres, edades y emails

cursor.execute("CREATE TABLE usuario1 (id INTEGER, nombre VARCHAR(100), apellido VARCHAR(100), cedula INTEGER, telefono INTEGER )")

cursor.execute("INSERT INTO usuario1 VALUES ( 1, 'Carlos', 'Gonzalez', 115269, 4440000)")

# Guardamos los cambios haciendo un commit
conexion.commit()

cursor.execute("SELECT * FROM usuario1")
usuario = cursor.fetchone()
print(usuario)

conexion.close()
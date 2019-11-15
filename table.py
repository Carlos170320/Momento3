import sqlite3

conexion = sqlite3.connect('ejemplo1.db')

# Creamos el cursor
cursor = conexion.cursor()

# Ahora crearemos una tabla de usuarios para almacenar nombres, edades y emails

cursor.execute("CREATE TABLE user1 (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(100), apellido VARCHAR(100), cedula INTEGER, telefono INTEGER )")

#usuarios = [
    #('1','Carlos', 'Gonzalez', 115269, 4440000),
    #('2','Carlos2', 'Gonzalez', 115269, 4440000),
    #('3','Carlos3', 'Gonzalez', 115269, 4440000),
    #('4','Carlos4', 'Gonzalez', 115269, 4440000),
#]

#cursor.executemany("INSERT INTO user1 VALUES ( ?,?,?, ?,?)", usuarios)

cursor.execute("SELECT * FROM user1")
usuarios = cursor.fetchall()
print(usuarios)

conexion.commit()
conexion.close()
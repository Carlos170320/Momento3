import sqlite3

conexion = sqlite3.connect('ejemplo1.db')
# Creamos el cursor
cursor = conexion.cursor()

cursor.execute("DELETE FROM user1 WHERE id='1'")

cursor.execute("SELECT * FROM user1")
usuarios = cursor.fetchall()
print(usuarios)


conexion.commit()
conexion.close()
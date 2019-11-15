import sqlite3

conexion = sqlite3.connect('ejemplo1.db')
# Creamos el cursor
cursor = conexion.cursor()

cursor.execute("UPDATE user1 SET nombre='David' WHERE id='1'")

cursor.execute("SELECT * FROM user1")
usuarios = cursor.fetchall()
print(usuarios)


conexion.commit()
conexion.close()
import sqlite3

conexion = sqlite3.connect('ejemplo1.db')
# Creamos el cursor
cursor = conexion.cursor()

usuarios = [
    ('1','Carlos', 'Gonzalez', 115269, 4440000),
    ('7','Carlos2', 'Gonzalez', 115269, 4440000),
    ('5','Carlos3', 'Gonzalez', 115269, 4440000),
    ('6','Carlos4', 'Gonzalez', 115269, 4440000),
]

cursor.executemany("INSERT INTO user1 VALUES ( ?,?,?, ?,?)", usuarios)
cursor.execute("SELECT * FROM user1")
usuarios = cursor.fetchall()
print(usuarios)

conexion.commit()
conexion.close()
import mysql.connector

HOST = "localhost"
USER = "USUARIO"#jconde
PASSWORD = "CLAVE"#julian2023!
BD = "NOMBRE_BASE_DE_DATOS"#nacidos

# Conectarse a la base de datos
conn = mysql.connector.connect(
    host=HOST,
    user=USER,
    password=PASSWORD,
    database=BD
)

# Crear un cursor
cursor = conn.cursor()

def cerrarConexion():
    cursor.close()
    conn.close()
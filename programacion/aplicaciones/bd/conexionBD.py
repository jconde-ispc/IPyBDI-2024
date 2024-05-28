import mysql.connector

HOST = "localhost"
USER = "USUARIO"#jconde
PASSWORD = "CLAVE"#julian2023!
BD = "NOMBRE_BASE_DE_DATOS"#nacidos

mydb = mysql.connector.connect(
  host=HOST,user=USER,
  password=PASSWORD,database=BD
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM persona")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)
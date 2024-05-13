import os
path = os.path.dirname(os.path.abspath(__file__)) + "/"

print("----------------------------------------------------------------")
print("Abra el archivo demo.txt y agregue contenido al archivo:")
#Abra el archivo "demofile2.txt" y agregue contenido al archivo:

f = open(path+"demo.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open(path+"demo.txt", "r")
print(f.read())
f.close()

print("----------------------------------------------------------------")
"""
Para crear un nuevo archivo en Python, use el open()método con uno de los siguientes parámetros:

"x"- Crear: creará un archivo, devuelve un error si el archivo existe.

"a"- Agregar: creará un archivo si el archivo especificado no existe

"w"- Escribir: creará un archivo si el archivo especificado no existe
"""

f = open(path+"demo2.txt", "a")#Si no existe, lo crea
f.write("Dejamos una linea nueva")
f.close()

f = open(path+"demo2.txt", "r")
print(f.read())
f.close()

f = open(path+"demo2.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open(path+"demo2.txt", "r")
print(f.read())
f.close()
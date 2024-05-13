import os

#path = "/home/usuario/desarrollo/proyectosISPC/IPyBDI-2024/programacion/ejemplosPython/archivos/"
path = os.path.dirname(os.path.abspath(__file__)) + "/"

"""
separador = os.path.sep
dir_actual = os.path.dirname(os.path.abspath(__file__))
dir = separador.join(dir_actual.split(separador)[:-1])
print(f"La direccion es {dir}\n y la direccion completa es {dir_actual}") 
"""

pathArchivo = path+"demo2.txt"

if os.path.exists(pathArchivo):
  os.remove(pathArchivo)
  print(f"Se elimino correctamente el archivo {pathArchivo}")
else:
  print(f"The file {pathArchivo} does not exist")



path = "/home/usuario/desarrollo/proyectosISPC/IPyBDI-2024/programacion/ejemplosPython/archivos/"
f = open(path+"demo.txt", "r")
print(f.read())
f.close()
print("----------------------------------------------------------------")
f = open(path+"demo.txt", "r")
print(f.read(5))
f.close()
print("----------------------------------------------------------------")
f = open(path+"demo.txt", "r")
for x in f:
  print(x)
f.close()


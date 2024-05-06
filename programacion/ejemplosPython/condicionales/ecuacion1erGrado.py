# https://colab.research.google.com/drive/1maCam3ltZrtzpwXws2dZTLiQNluoK2V6?usp=sharing
# Valores para Dibujar la Tabla
ANCHO = 40
RELLENO1 = "-"
RELLENO2 = " "
CADENA_VACIA = ""
 
######################################################################
 
MENSAJE_INICIAL = "ECUACION DE PRIMER GRADO: ax + b = 0"
 
######################################################################
 
# Declaracion de variables
a = 0 # Coeficiente principal
b = 0 # Termino Independiente
x = 0 # Incognita
 
# Formato de Salida Final en Pantalla
Formato_Ecuacion = "ECUACION: {} x + {} = 0"
 
######################################################################
 
# Encabezado del Programa
print(CADENA_VACIA.center(ANCHO,RELLENO1))
print(MENSAJE_INICIAL.center(ANCHO,RELLENO2))
print(CADENA_VACIA.center(ANCHO,RELLENO1))
 
######################################################################
 
# Inicio del Programa:
a = float(input(">>> Valor de a: "))
b = float(input(">>> Valor de b: "))
 
print(CADENA_VACIA.center(ANCHO,RELLENO1))
print(Formato_Ecuacion.format(a,b))
print(CADENA_VACIA.center(ANCHO,RELLENO1))
 
try:
    x = -b/a
    print(">>> SOLUCION: x = ", x)
except:
    if b != 0:
        print("La ECUACION no tiene solucion.")
    else:
        print("La ECUACION tiene infinitas soluciones.")
 
######################################################################
 
print(CADENA_VACIA.center(ANCHO,RELLENO1))
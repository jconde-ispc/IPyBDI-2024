# https://colab.research.google.com/drive/1AG8nDCuYtHw2asnJljt-kFaFLwSmd33b?usp=sharing
# Importacion de librerias
from math import sqrt
 
######################################################################
 
# Valores para Dibujar la Tabla
ANCHO = 55
RELLENO1 = "-"
RELLENO2 = " "
CADENA_VACIA = ""
 
######################################################################
 
MENSAJE_INICIAL = "ECUACION DE SEGUNDO GRADO: ax^2 + bx + c = 0"
 
######################################################################
 
# Declaracion de Variables
a, b, c = 0, 0, 0
x1, x2  = 0.0, 0.0
discriminante = 0
 
######################################################################
 
# Encabezado del Programa
print(CADENA_VACIA.center(ANCHO,RELLENO1))
print(MENSAJE_INICIAL.center(ANCHO,RELLENO2))
print(CADENA_VACIA.center(ANCHO,RELLENO1))
 
######################################################################
 
# Solicitud de Datos 
a = float(input(">>> Valor de a: "))
b = float(input(">>> Valor de b: "))
c = float(input(">>> Valor de c: "))
 
discriminante = b**2 - 4*a*c
 
try:
    x1 = (-b + sqrt(discriminante)) / (2 * a)
    x2 = (-b - sqrt(discriminante)) / (2 * a)
 
    print(CADENA_VACIA.center(ANCHO,RELLENO1))
 
    if x1 == x2:
        print(">>> SOLUCION: x = %4.2f" % x1)
    else:
        print(">>> SOLUCIONES: x1 = %4.2f y x2 = %4.2f" % (x1, x2))
 
except ZeroDivisionError:
 
    print(CADENA_VACIA.center(ANCHO,RELLENO1))
 
    if b != 0:
        print("La ecuacion no tiene solucion.")
    else:
        print("La ecuacion tiene infinitas soluciones.")
 
except ValueError:
    # Casos:
    # 1) Se produce una division por cero.
    # 2) Se produce por calcular la raız cuadrada de un discriminante
    # negativo.
    print(CADENA_VACIA.center(ANCHO,RELLENO1))
    print("No hay soluciones reales")
 
######################################################################
 
print(CADENA_VACIA.center(ANCHO,RELLENO1))
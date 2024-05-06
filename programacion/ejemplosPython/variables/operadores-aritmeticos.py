# Ejercicio de desafío con Operadores Aritméticos
#1) Definir 4 variables del tipo String manualmente (Sin solicitarlas al usuario). Por ejemplo:

str_Precio1 = "11111111"
str_Precio2 = "22222222"
str_Precio3 = "33333333"
str_Precio4 = "44444444"


# 2) Transformar cada valor a un entero y sumarlos en una variable: ( La suma no debe ser mayor a 999.999.999)

int_Total = int(str_Precio1) + int(str_Precio2) + int(str_Precio3) + int(str_Precio4) 


#3) Calcular la parte entera y la parte decimal como se explica en la clase: (6E+3D)

int_Parte_Entera = int_Total / 1000 
int_Parte_Decimal = int_Total % 1000 


#4) Mostrar un mensaje con los valores en pantalla representando el número completo con sus decimales.

print("Precio(6E+3D): %d.%03d" %(int_Parte_Entera,int_Parte_Decimal))
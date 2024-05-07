# Declaracion de Variables
suma = 0.0
numero = 0
 
# Solicitud de Datos
print("Introduce un número entero: ")
numero = int(input("> "))
 
# Cálculo de la suma
suma = numero * (numero + 1) / 2
print("La suma desde 1 hasta " + str(numero) + " es " + str(suma))
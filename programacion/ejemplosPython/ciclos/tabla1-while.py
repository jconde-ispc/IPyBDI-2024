# https://colab.research.google.com/drive/12bidgiIPJwXZdVpr749ps2tgd4HKZgnR?usp=sharing
# Declaracion de variables
multiplicador = 1
resultado = 0
numero = 0
 
# Solicitud de Datos
numero = int(input('>>> Introduce el numero a multiplicar: '))
 
while multiplicador > 0 and multiplicador < 11:
    resultado = numero * multiplicador
    print("%d x %2d = %d" %(numero,multiplicador,resultado))
    multiplicador = multiplicador + 1
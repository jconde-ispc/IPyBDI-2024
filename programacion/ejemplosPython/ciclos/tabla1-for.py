# https://colab.research.google.com/drive/12bidgiIPJwXZdVpr749ps2tgd4HKZgnR?usp=sharing
# Solicitud de Datos
numero = int(input('>>> Introduce el numero a multiplicar: '))
 
for multiplicador in range(1,11):
    resultado = numero * multiplicador
    print("%d x %2d = %d" % (numero,multiplicador,resultado))
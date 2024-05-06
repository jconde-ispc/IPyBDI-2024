# https://colab.research.google.com/drive/1zQHDORxdTyYZDJGukz0MKTiuErGVwoof?usp=sharing
# Declaracion de variables
potencia = 1
resultado = 0
numero = 0
 
# Solicitud de datos
numero = int(input('>>> Introduce el numero a elevar: '))
 
while potencia > 0 and potencia  < 11:
    resultado= numero ** potencia
    print("%d elevado a %2d es %d"%(numero,potencia,resultado))
    potencia = potencia + 1
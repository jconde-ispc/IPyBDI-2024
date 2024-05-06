# https://colab.research.google.com/drive/1zQHDORxdTyYZDJGukz0MKTiuErGVwoof?usp=sharing
# Solicitud de Datos
numero = int(input('>>> Introduce el numero a elevar: '))
 
for potencia in range(1,11):
    resultado= numero ** potencia
    print("%d elevado a %2d es %d"%(numero,potencia,resultado))
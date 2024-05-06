# https://colab.research.google.com/drive/1Wi7MLWxmoJ7cnuIlKi_vjHgqPDyTi-eV?usp=sharing
# Declaracion de variables
primer_numero  = 0.0
segundo_numero = 0.0
tercer_numero  = 0.0
cuarto_numero  = 0.0
quinto_numero  = 0.0
 
# Solicitud de datos
primer_numero  = float(input('Introduce el Primer  numero: '))
segundo_numero = float(input('Introduce el Segundo numero: '))
tercer_numero  = float(input('Introduce el Tercer  numero: '))
cuarto_numero  = float(input('Introduce el Cuarto  numero: '))
quinto_numero  = float(input('Introduce el Quinto  numero: '))
 
posible_maximo = primer_numero
 
if segundo_numero > posible_maximo:
    posible_maximo = segundo_numero
 
if tercer_numero > posible_maximo:
    posible_maximo = tercer_numero
 
if cuarto_numero > posible_maximo:
    posible_maximo = cuarto_numero
 
if quinto_numero > posible_maximo:
    posible_maximo = quinto_numero
 
maximo = posible_maximo
 
print ('>>> El Numero maximo es: %5.2f' %(maximo))

# https://colab.research.google.com/drive/1BjgwlASaonzZ3RjD2iCp010F1ltjSvtd?usp=sharing

# Declaracion de variables
primer_numero  = 0.0
segundo_numero = 0.0
tercer_numero  = 0.0

# Solicitud de datos
primer_numero  = float(input('Introduce el primer  numero: '))
segundo_numero = float(input('Introduce el segundo numero: '))
tercer_numero  = float(input('Introduce el tercer  numero: '))

if primer_numero > segundo_numero:
    if primer_numero > tercer_numero:
        maximo = primer_numero
    else:
        maximo = tercer_numero
else:
    if segundo_numero > tercer_numero:
        maximo = segundo_numero
    else:
        maximo = tercer_numero

print('>>> El numero maximo es: %5.2f' %(maximo))
# https://colab.research.google.com/drive/19yNW1sa5TMPXq5aDnv2t6qClzkK1_uBs?usp=sharing

# Declaracion de variables
letra = ''

# Solicitud de Datos
letra = input('>>> Introduce una letra: ')

if letra <= 'z'  and letra >= 'a':  # a-z (97-122)
    print('La letra es minuscula.')

elif letra <= 'Z' and letra >= 'A':  # A-Z (65-90)
    print('La letra es Mayuscula.')
else:
    print('El valor introducido no es una letra.')
# https://colab.research.google.com/drive/1YY7crmvqZdDpAgBrztoqqPnKQopItllT?usp=sharing

# Declaracion de variables:
int_Numero = 0

# Solicitud de Datos 
int_Numero = int(input('>>> Introduce un numero: '))

if int_Numero == (int_Numero // 3) * 3:
    print("El numero %d es multiplo de 3." %(int_Numero))
else:
    print("El numero %d no es multiplo de 3." %(int_Numero))
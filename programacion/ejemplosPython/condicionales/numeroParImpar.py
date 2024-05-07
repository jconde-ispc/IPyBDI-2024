# https://colab.research.google.com/drive/1FhbSGiIu7ZdBrmrmx6nHyGBdPZb35PuQ?usp=sharing

# Declaracion de variables:
int_Numero = 0

# Solicitud de Datos
int_Numero = int(input('>>> Introduce un numero: '))

if int_Numero == (int_Numero // 2) * 2:
    print(f"El numero {int_Numero} es par.")
else:
    print(f"El numero {int_Numero} es impar.")
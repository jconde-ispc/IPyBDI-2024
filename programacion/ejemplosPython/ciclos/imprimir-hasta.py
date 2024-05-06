# https://colab.research.google.com/drive/1RNh94AKvSvzbX6fLPBpixwRJkFReCVmP?usp=sharing
# Solicitud de Datos
numero = int(input('>>> Introduce un numero: '))
 
for pares in range(0,numero + 1):
    if pares == int(pares/2)*2 and pares>0:
        print(pares)
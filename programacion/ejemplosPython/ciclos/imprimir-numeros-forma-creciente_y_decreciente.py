# https://colab.research.google.com/drive/10FO_IbizkQPy5aaD2V_M6NswbbTp-wt1?usp=sharing
print('Imprimir los numeros pares entre 0 y 200 de forma Creciente')
 
for pares in range(0,201):
    if pares == int(pares/2)*2 and pares>0:
        print(pares)


# https://colab.research.google.com/drive/1zGe2-km4dlH3XiyaueZ4lQtSvEjvq22O?usp=sharing
print('Imprimir los numeros pares entre 0 y 200 de forma decreciente')
 
for pares in range(200,-1,-1):
    if pares == int(pares/2)*2 and pares > 0:
        print(pares)
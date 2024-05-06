# https://colab.research.google.com/drive/1DmYxWluM7vtAmo3yzoiCtAqBeyjDPsT5?usp=sharing
# Declaracion de variables
primer_numero  = 0.0
segundo_numero = 0.0
tercer_numero  = 0.0
cuarto_numero  = 0.0
quinto_numero  = 0.0
 
Resta1 = 0.0
Resta2 = 0.0
Resta3 = 0.0
Resta4 = 0.0
 
# Solicitud de datos
primer_numero  = int(input('Introduce el Primer  numero: '))
segundo_numero = int(input('Introduce el Segundo numero: '))
tercer_numero  = int(input('Introduce el Tercer  numero: '))
cuarto_numero  = int(input('Introduce el Cuarto  numero: '))
quinto_numero  = int(input('Introduce el Quinto  numero: '))
 
# Se realizan las restas para hallar la menor diferencia
Resta1 = primer_numero - segundo_numero
Resta2 = primer_numero - tercer_numero
Resta3 = primer_numero - cuarto_numero
Resta4 = primer_numero - quinto_numero
 
menor_diferencia = Resta1
 
if Resta2 < menor_diferencia and Resta2 >= 0:
   menor_diferencia = Resta2
else:
    if Resta2 > menor_diferencia and Resta2 <= 0:
        menor_diferencia = Resta2
 
if Resta3 < menor_diferencia and Resta3 >= 0:
   menor_diferencia = Resta3
else:
    if Resta3 > menor_diferencia and Resta3 <= 0:
        menor_diferencia = Resta3
 
if Resta4 < menor_diferencia and Resta4 >= 0:
   menor_diferencia = Resta4
else:
    if Resta4 > menor_diferencia and Resta4 <= 0:
        menor_diferencia = Resta4
 
numero_cercano = primer_numero - menor_diferencia
 
print('El numero mas cercano a %d es %d'%(primer_numero,numero_cercano))
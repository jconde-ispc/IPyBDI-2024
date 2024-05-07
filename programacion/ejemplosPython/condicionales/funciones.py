import random

def pedirNumero():
    while True:
        try:
            x = int(input('Enter a number: '))
            break
        except ValueError:
            print('This is not a number, try again.')
    
    return x

def aleatorio(n):
    for i in range (20): 
        print(random.randrange(n))

#aleatorio(5)

def saludar(nombre,mensaje):
    print("Hola "+nombre+" !!!")
    print(mensaje)
x= 2
y= 4

#definicion de la funcion sumar
def sumaInput():
    print("Ingreso a funcion sumaInput")
    x = int(input('Ingrese el primer numero: '))
    y = int(input('Ingrese el segundo numero: '))
    resultado = x + y
    print(f"El valor de sumar {x} + {y} es {resultado}")
    
    print (resultado)

def suma(x,y) -> int:
    print(f"Ingreso a funcion suma con los parametros: {x} y {y}")   
    resultado = x + y
    print(f"El valor de sumar {x} + {y} es {resultado}")
    return resultado


def suma2():
    
    print(f"x local {x}")
    print(id(x))
    print(y)
    print(id(y))


suma2()
print(f"x global {x}")
print(id(x))
print(id(y))

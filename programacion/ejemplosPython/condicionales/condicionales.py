import funciones


def condicional1():
    number = funciones.pedirNumero()
        
    if number > 2:
        print("Number is bigger than 2.")
    elif number < 2: # Optional clause (you can have multiple elifs)
        print("Number is smaller than 2.")
    else: # Optional clause (you can only have one else)
        print("Number is 2.")
    print("Number is:",number)

#INVOCACIONES
condicional1()

print("-----------1--------------")

a= 1
b= 6
if a and b > 2:
    print('yes')
else:
    print('no')

print("-----------2--------------")

if a > 2 and b > 2:
    print('yes')
else:
    print('no')

print("-----------3--------------")

if a == 3 or 4 or 6:
    print('yes')
else:
    print('no')

print("-----------4--------------")
if a == 3 or a == 4 or a == 6:
      print('yes')
else:
    print('no')

print("-----------5--------------")
if a in (3, 4, 6):
    print('yes')
else:
    print('no')

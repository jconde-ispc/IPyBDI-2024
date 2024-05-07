from array import *
print("------------1-------------")
my_array = array('i', [1,2,3,4,5])
print(my_array[1])
# 2
print(my_array[2])
# 3
print(my_array[0])
# 1

print("------------2-------------")
for i in my_array:
    print(i)
# 1
# 2
# 3
# 4
# 5

#Funcion para reutilizar el bloque de código als veces que desee
def imprimirArreglo(a):
    for i in a:
        print(i)

print("-----------3--------------")
my_array.append(6)
imprimirArreglo(my_array)
# array('i', [1, 2, 3, 4, 5, 6])

print("-----------4--------------")

def func(*args):
# args will be a tuple containing all values that are passed in
    for i in args:
        print(i)

func(1, 2, 3)
# Calling it with 3 arguments
# Out: 1
# 2
# 3
print("-----------5--------------")

list_of_arg_values = [1, 2, 3, 4]
func(*list_of_arg_values) # Calling it with list of values, * expands the list
# Out: 1
#2
#3

print("-----------6--------------")

func() # Calling it without arguments
# No Output



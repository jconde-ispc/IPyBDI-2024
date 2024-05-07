#TUPLAS
""" 
Las tuplas se utilizan para almacenar varios elementos en una sola variable.
Tuple es uno de los 4 tipos de datos integrados en Python que se utilizan para almacenar colecciones de datos; los otros 3 son List , Set y Dictionary , todos con diferentes calidades y usos.
Una tupla es una colección ordenada e inmutable .
Las tuplas se escriben entre paréntesis.


Elementos de tupla
Los elementos de tupla están ordenados, no se pueden modificar y permiten valores duplicados.
Los elementos de tupla están indexados, el primer elemento tiene índice [0], el segundo elemento tiene índice [1], etc.

Ordenado
Cuando decimos que las tuplas están ordenadas, significa que los elementos tienen un orden definido y ese orden no cambiará.

Inmutable
Las tuplas no se pueden cambiar, lo que significa que no podemos cambiar, agregar o eliminar elementos una vez creada la tupla.

Permitir duplicados
Como las tuplas están indexadas, pueden tener elementos con el mismo valor:
"""

thistuple = ("apple", "banana", "cherry")#Crea una tupla
print(thistuple)

thistuple = ("apple", "banana", "cherry", "apple", "cherry") #Las tuplas permiten valores duplicados
print(thistuple)

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))#Para determinar cuántos elementos tiene una tupla, use la len()función

#Create Tuple With One Item. To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#Tuple items can be of any data type:

#String, int and boolean data types:
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

#A tuple can contain different data types:
tuple1 = ("abc", 34, True, 40, "male")

#type()
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

#The tuple() Constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)


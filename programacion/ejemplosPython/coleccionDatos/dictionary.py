""" 
Hay cuatro tipos de datos de recopilación en el lenguaje de programación Python:

La lista es una colección ordenada y modificable. Permite miembros duplicados.
Tupla es una colección ordenada e inmutable. Permite miembros duplicados.
Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
El diccionario es una colección ordenada** y modificable. No hay miembros duplicados.
* Los elementos establecidos no se pueden cambiar, pero puedes eliminar y/o agregar elementos cuando quieras.
**A partir de la versión 3.7 de Python, los diccionarios están ordenados . En Python 3.6 y versiones anteriores, los diccionarios están desordenados .

Al elegir un tipo de colección, resulta útil comprender las propiedades de ese tipo. Elegir el tipo correcto para un conjunto de datos en particular podría significar la retención del significado y podría significar un aumento en la eficiencia o la seguridad.

DICCIONARIO

Los diccionarios se utilizan para almacenar valores de datos en pares clave:valor.
Un diccionario es una colección ordenada*, modificable y que no permite duplicados.
A partir de la versión 3.7 de Python, los diccionarios están ordenados . En Python 3.6 y versiones anteriores, los diccionarios están desordenados .
Los diccionarios están escritos entre llaves y tienen claves y valores

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

Elementos del diccionario
Los elementos del diccionario están ordenados, modificables y no permiten duplicados.
Los elementos del diccionario se presentan en pares clave:valor y se puede hacer referencia a ellos mediante el nombre de la clave.

¿Ordenado o desordenado?
Cuando decimos que los diccionarios están ordenados, significa que los elementos tienen un orden definido y ese orden no cambiará.
Desordenado significa que los elementos no tienen un orden definido, no se puede hacer referencia a un elemento mediante un índice.

Cambiable
Los diccionarios se pueden cambiar, lo que significa que podemos cambiar, agregar o eliminar elementos una vez creado el diccionario.

Duplicados no permitidos
Los diccionarios no pueden tener dos elementos con la misma clave

Elementos del diccionario: tipos de datos
Los valores de los elementos del diccionario pueden ser de cualquier tipo de datos
"""

d = {'a': 1, 'b': 2, 'c':3}
for key in d:
    print(key, d[key])
# c 3
# b 2
# a 1


print([key for key in d])
# ['c', 'b', 'a']

for key, value in d.items():
    print(key, value)
# c 3
# b 2
# a 1


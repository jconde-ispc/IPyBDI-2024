import numpy
import matplotlib.pyplot as plt
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
print(f"Dado el siguiente arreglo (lista):{type(speed)}: {speed}")

#El valor medio es el valor medio.
#Para calcular la media, encuentre la suma de todos los valores y divida la suma por el número de valores:
valorMedio = numpy.mean(speed)
print(f"El valor medio es: {valorMedio}")

#El valor mediano es el valor en el medio, después de haber ordenado todos los valores:
mediana = numpy.median(speed)
print(f"Mediana:{type(mediana)} {mediana}")

#Moda. El valor de Moda es el valor que aparece la mayor cantidad de veces:
moda = stats.mode(speed)
print(f"El valor Moda es:{type(moda)} {moda}")

#Desviación standard y varianza:
"""
La desviación estándar es un número que describe qué tan dispersos están los valores.
Una desviación estándar baja significa que la mayoría de los números están cerca del valor medio (promedio).
Una desviación estándar alta significa que los valores se distribuyen en un rango más amplio.

La varianza es otro número que indica qué tan dispersos están los valores.
De hecho, si tomas la raíz cuadrada de la varianza, ¡obtienes la desviación estándar!
O al revés, si multiplicas la desviación estándar por sí misma, ¡obtienes la varianza!
"""
nuevoSpeed = [86,87,88,86,87,85,86]
desviacionStandard = numpy.std(nuevoSpeed)
varianza = numpy.var(nuevoSpeed)
print(f"La desviación estandar de {nuevoSpeed} es {desviacionStandard} y la varianza {varianza}")

otroSpeed = [32,111,138,28,59,77,97]
desviacionStandard = numpy.std(otroSpeed)
varianza = numpy.var(otroSpeed)
print(f"La desviación estandar de {otroSpeed} es {desviacionStandard} y la varianza {varianza}")

#Percentiles
""""
Los percentiles se utilizan en estadística para darle un número que describe el valor al que un porcentaje determinado de los valores es inferior.
Ejemplo: Digamos que tenemos un conjunto de edades de todas las personas que viven en una calle.
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
¿Cuál es el percentil 75? La respuesta es 43, lo que significa que el 75% de las personas tienen 43 años o menos.
"""
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
x = numpy.percentile(ages, 75)
print(f"Dada la lista de edades: {ages} el percentil de 75 es {x}")

print("¿Cuál es la edad que tiene el 90% de las personas más jóvenes? numpy.percentile(ages, 90)")
x = numpy.percentile(ages, 90)
print(f"el percentil de 90 es {x}")

""""
¿Cómo podemos obtener grandes conjuntos de datos?
Para crear grandes conjuntos de datos para pruebas, utilizamos el módulo de Python NumPy, que viene con varios métodos para crear conjuntos de datos aleatorios, de cualquier tamaño.
"""
x = numpy.random.uniform(0.0, 5.0, 250)

plt.hist(x, 5)
plt.show()

"""
Histograma explicado
Usamos la matriz del ejemplo anterior para dibujar un histograma con 5 barras.
La primera barra representa cuántos valores de la matriz están entre 0 y 1.
La segunda barra representa cuántos valores hay entre 1 y 2.
"""

#Distribución normal
"""Usamos la matriz del numpy.random.normal() método, con 100000 valores, para dibujar un histograma con 100 barras.

Especificamos que el valor medio es 5,0 y la desviación estándar es 1,0.

Lo que significa que los valores deberían concentrarse alrededor de 5,0 y rara vez más lejos de 1,0 de la media.

Y como puede ver en el histograma, la mayoría de los valores están entre 4,0 y 6,0, con un máximo aproximadamente en 5,0."""

x = numpy.random.normal(5.0, 1.0, 100000)

plt.hist(x, 100)
plt.show()

#Grafico de dispersión
#Un diagrama de dispersión es un diagrama donde cada valor del conjunto de datos está representado por un punto.
"""El módulo Matplotlib tiene un método para dibujar diagramas de dispersión, necesita dos matrices de la misma longitud, una para los valores del eje x y otra para los valores del eje y:

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]

y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

La xmatriz representa la edad de cada automóvil.

La ymatriz representa la velocidad de cada automóvil."""


x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x, y)
plt.show()

"""
El eje x representa edades y el eje y representa velocidades.
Lo que podemos leer en el diagrama es que los dos autos más rápidos tenían 2 años y el auto más lento tenía 12 años.
Nota: Parece que cuanto más nuevo es el coche, más rápido se conduce, pero eso podría ser una coincidencia, después de todo sólo registramos 13 coches.
"""

"""
Distribuciones aleatorias de datos
En Machine Learning, los conjuntos de datos pueden contener miles, o incluso millones, de valores.

Es posible que no tenga datos del mundo real cuando pruebe un algoritmo, es posible que deba utilizar valores generados aleatoriamente.

Como aprendimos en el capítulo anterior, ¡el módulo NumPy puede ayudarnos con eso!

Creemos dos matrices que estén llenas con 1000 números aleatorios de una distribución de datos normal.

La primera matriz tendrá la media establecida en 5,0 con una desviación estándar de 1,0.

La segunda matriz tendrá la media establecida en 10,0 con una desviación estándar de 2,0:
"""
x = numpy.random.normal(5.0, 1.0, 1000)
y = numpy.random.normal(10.0, 2.0, 1000)

plt.scatter(x, y)
plt.show() 

"""
Diagrama de dispersión explicado
Podemos ver que los puntos se concentran alrededor del valor 5 en el eje x y 10 en el eje y.
También podemos ver que la extensión es mayor en el eje y que en el eje x.
"""

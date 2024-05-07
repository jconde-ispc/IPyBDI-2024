# https://colab.research.google.com/drive/1OLpsWf8AHDv5LnqSh_T853WJGfDfcLy_?usp=sharing
# Declaracion de Variables:
M = []
longitud = 0
dimension = 0
 
######################################################################
 
# Pedimos la dimensión de la matriz,
dimension = int(input(">>> Dimension de la matriz de tamaño n x n: "))
 
# Creamos una matriz nula...
for elemento in range(dimension):
        M.append ([0] * dimension)
 
# ... y leemos su contenido
for fila in range(dimension):
    for columna in range(dimension):
        # Si el numero de fila y columna es igual
        if fila == columna:
             # Guarda el número 1 en la posición
             M[fila][columna] = 1
 
######################################################################
 
print("\n>>> MATRIZ M(%dx%d): %s\n" %(dimension,dimension,M))
 
longitud = len(M)
 
# Se imprime cada fila de la matriz
for valor in range(longitud):
    print(M[valor])
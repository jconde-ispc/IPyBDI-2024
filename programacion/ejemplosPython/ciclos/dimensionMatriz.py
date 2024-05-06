# https://colab.research.google.com/drive/1YL6GM-GfTQDE1BTkZzQeUTdWg-FsaFsX?usp=sharing
# Declaracion de Variables:
Matriz = []
Longitud = 0
 
# Creacion de la matriz 
Matriz = [[7, 8, 9], [4, 5, 6,], [7, 8, 9]]
 
# Longitud de la Matriz
Longitud = len(Matriz)
 
print(">>> MATRIZ: %s" %(Matriz))
 
# Se imprime cada fila de la matriz
for fila in range(Longitud):
    print(">>> FILA %d: %s" %(fila+1, Matriz[fila]))
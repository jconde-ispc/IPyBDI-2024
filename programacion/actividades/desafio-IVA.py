"""
Desarrollar un programa secuencial que permita ingresar un precio
calcular el IVA y mostrar el precio final de lista de un producto
Ejemplo: Si un producto vale $100 y el IVA es 21, el precio de lista es $121
"""

# Ingresar el precio del producto
precio = float(input("Ingrese el precio del producto: "))

# Calcular el IVA
iva = float(input("Ingrese el valor del IVA: "))

incremento_por_iva = (precio * (iva / 100))
# Mostrar el incremento por el IVA
print("El incremento del producto por el IVA: $" + str(incremento_por_iva))

precio_con_iva = precio + incremento_por_iva

# Mostrar el precio final de lista
print("El precio de lista del producto es: $" + str(precio_con_iva))
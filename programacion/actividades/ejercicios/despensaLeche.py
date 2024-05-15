"""
Una despensa de barrio vende la leche de vaca entera de litro a 1000 pesos
la unidad. Si el cliente compra más de 12  unidades (y hasta 24 unidades),
el costo tiene un descuento del 10%. Si compra más de 24 unidades, el 
descuento es del 15%. Además posee la promoción a los jubilados.
La promoción de jubilados es sumarle un 10% de descuento (si posee otros 
descuentos, se suma los descuentos).
Desarrolle una solución algorítmica para saber cuento debe pagar el cliente.
"""

"""Analisis:
EPS
Entrada: unidadesDeLeche E entero, esJubiado E Logico
Salida: montoAPagar E Real
Proceso:
montoParcial E Real
montoParcial = unidadesDeLeche * 1000

montoAPagar = montoParcial si el cliente compra hasta 12 unidades y no es jubilado
montoAPagar = montoParcial * 0,9 (o montoParcial - montoParcial * 0,10) si el cliente compra mas de 12 unidades y hasta 24. Y no es jubilado
montoAPagar = montoParcial * 0,85 si el cliente compra mas de 24 unidades. Y no es jubilado

montoAPagar = montoParcial * 0,9 si el cliente compra hasta 12 unidades y es jubilado
montoAPagar = montoParcial * 0,8 si el cliente compra mas de 12 unidades y hasta 24. Y es jubilado
montoAPagar = montoParcial * 0,75 si el cliente compra mas de 24 unidades. Y es jubilado
...
"""
unidadesDeLeche = int(input("Ingrese la cantidad de unidades de leche que compra el cliente"))
esJubiado = int(input("Ingrese 0 si el cliente no es jubilado, cualquier otro numero si el cliente es Jubilado"))

montoParcial = unidadesDeLeche * 1000
print(f"unidadesDeLeche {unidadesDeLeche} esJubiado {esJubiado}")

if(unidadesDeLeche <=12 and not esJubiado):
    print("unidadesDeLeche <=12 and not esJubiado")
    montoAPagar = montoParcial
elif((unidadesDeLeche >12 and unidadesDeLeche <= 24) and not esJubiado):
    print("(unidadesDeLeche >12 and unidadesDeLeche <= 24) and not esJubiado")
    montoAPagar = montoParcial * 0.9
elif(unidadesDeLeche > 24 and not esJubiado):
    print("unidadesDeLeche > 24 and not esJubiado")
    montoAPagar = montoParcial * 0.85
if(unidadesDeLeche <=12 and esJubiado):
    print("unidadesDeLeche <=12 and esJubiado")
    montoAPagar = montoParcial * 0.9
elif((unidadesDeLeche >12 and unidadesDeLeche <= 24) and esJubiado):
    print("(unidadesDeLeche >12 and unidadesDeLeche <= 24) and esJubiado")
    montoAPagar = montoParcial * 0.8
elif(unidadesDeLeche > 24 and esJubiado):
    print("unidadesDeLeche > 24 and esJubiado")
    montoAPagar = montoParcial * 0.75

print(f"El monto sin descuento es: {montoParcial} y el monto total a pagar es: {montoAPagar}")

#Agregar pruebas

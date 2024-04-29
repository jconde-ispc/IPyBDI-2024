# Declaracion de Variables
float_pesos = 0.0
float_dolares = 0.0
float_tipoCambio = 0.0

# Incio del programa
print("CASA DE CAMBIOS")

# SOLICITUD de Datos 
float_pesos = int(input('Introduzca el monto en pesos argentinos: '))
float_tipoCambio = int(input('Introduzca a cuántos pesos argentinos equivale 1 dólar: '))

float_dolares = float_pesos / float_tipoCambio

print("Los {0} pesos argentinos equivalen a {1:.2f} dólares teniendo en cuenta el valor del dólar({2}):"
        .format(float_pesos, round(float_dolares, 2), float_tipoCambio))

# :.2f  dentro de las llaves en el print para especificar que se deben mostrar solo dos decimales en el valor de  float_dolares
# la función  round()  para redondear el valor de  float_dolares  a dos decimales
# Declaracion de Constantes
PI = 3.1416 # Valor aproximado de PI
 
# Declaracion de Variables
int_Radio  = 0
float_Area = 0
 
# Incio del programa
print("CALCULAR EL AREA DEL CIRCULO")
 
# SOLICITUD de Datos 
int_Radio = int(input('Introduzca el radio del circulo: '))
 
# AREA DE UN CIRCULO
float_Area = PI*(int_Radio**2)
 
print("El area del circulo es:  %0.2f"%(float_Area))
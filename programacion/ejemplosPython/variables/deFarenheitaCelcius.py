# Declaracion de Variables
int_farenheit = 0
float_celcius = 0.0
 
# Incio del programa
print("LLEVAR GRADOS FARENHEIT A CELCIUS")
 
# SOLICITUD de Datos 
int_farenheit = int(input('Introduzca los grados Farenheit: '))
 
# FAHRENHEIT A CELCIUS
float_celcius = (int_farenheit-32.0)*5.0/9.0
 
print("Grados Celsius:  %0.2f"%(float_celcius))
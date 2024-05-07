# Valores para Dibujar la Tabla
ANCHO = 40
RELLENO1 = "-"
RELLENO2 = " "
CADENA_VACIA = ""
 
######################################################################
 
# Mensajes a Mostrar
MENSAJE_INICIAL = "RADAR DE VELOCIDAD"
 
######################################################################
 
# Declaracion de variables
Velocidad   = 0.0
Frecuencia0 = 2e-10            
Frecuencia1 = 2.0000004e-10    
 
# Formato de Salida Final en Pantalla
Formato_Respuesta = ">>> La Velocidad es: %0.2f millas/hora."
 
######################################################################
 
# Encabezado del Programa
# LINEA 1: Parte superior de la Tabla
print(CADENA_VACIA.center(ANCHO,RELLENO1))
# Mensaje Centrado
print(MENSAJE_INICIAL.center(ANCHO,RELLENO2))
 
######################################################################
 
# Inicio del Programa:
# Calculo de la VELOCIDAD del radar
# velocidad = 6.685x10^8 x (f1 - f0) / (f1 + f0)
Velocidad=6.685e8*(Frecuencia1-Frecuencia0)/(Frecuencia1+Frecuencia0)
 
# LINEA 2: Separador de la tabla
print(CADENA_VACIA.center(ANCHO,RELLENO1))
# Se muestra el mensaje en Pantalla
print(Formato_Respuesta.center(ANCHO,RELLENO2) %(Velocidad))
 
######################################################################
 
# LINEA 3: Parte Inferior de la Tabla
print(CADENA_VACIA.center(ANCHO,RELLENO1))
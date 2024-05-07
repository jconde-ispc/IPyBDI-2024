# Valores para Dibujar la Tabla
ANCHO = 40
RELLENO1 = "-"
RELLENO2 = " "
CADENA_VACIA = ""
 
######################################################################
 
# Declaracion de Constantes
HORAS_SEMANALES = 40
HORAS_MENSUALES = 160
 
######################################################################
 
# Mensajes a Mostrar
MENSAJE_INICIAL = "CALCULADORA FREELANCER (USD)"
# Mensajes de solicitud de Datos
SOLICITAR_PRECIO = ">>> Precio en dolares por Hora: "
# Mensajes de Error
ERROR_FORMATO = "SOLO SE PERMITEN NUMEROS"
 
######################################################################
 
# Declaracion de variables
Pago_Semanal, Pago_Mensual , Dolares_Por_Hora,  = 0.0 , 0.0, 0.0
# Formato de Salida Final en Pantalla
Formato_Respuesta = ">>> PAGO SEMANAL: %4.2f\n>>> PAGO MENSUAL: %4.2f"
 
######################################################################
 
# Encabezado del Programa
# LINEA 1: Parte superior de la Tabla
print(CADENA_VACIA.center(ANCHO,RELLENO1))
# Mensaje Centrado
print(MENSAJE_INICIAL.center(ANCHO,RELLENO2))
# LINEA 2: Separador de la tabla
print(CADENA_VACIA.center(ANCHO,RELLENO1))
 
######################################################################
 
# Inicio del Programa:
try:
    # Solicitud de Datos
    Dolares_Por_Hora   = float(input(SOLICITAR_PRECIO))
 
    # Cálculos para el pago Semanal y Mensual
    Pago_Semanal = Dolares_Por_Hora * HORAS_SEMANALES
    Pago_Mensual = Dolares_Por_Hora * HORAS_MENSUALES
 
    # LINEA 3: Separador de la tabla
    print(CADENA_VACIA.center(ANCHO,RELLENO1))
 
    # Se muestra el mensaje en Pantalla
    print(Formato_Respuesta %(Pago_Semanal,Pago_Mensual))
 
except ValueError:
    print(CADENA_VACIA.center(ANCHO,RELLENO1))
    print(ERROR_FORMATO.center(ANCHO,RELLENO2))
 
######################################################################
 
# LINEA 4: Parte Inferior de la Tabla
print(CADENA_VACIA.center(ANCHO,RELLENO1))
"""
Una despensa de barrio vende la leche de vaca entera de litro a 1000 pesos
la unidad. Si el cliente compra más de 12  unidades (y hasta 24 unidades),
el costo tiene un descuento del 10%. Si compra más de 24 unidades, el 
descuento es del 15%. Además posee la promoción a los jubilados.
La promoción de jubilados es sumarle un 10% de descuento (si posee otros 
descuentos, se suma los descuentos).
Desarrolle una solución algorítmica para saber cuento debe pagar el cliente.
"""
#Docstring
# __doc__ (Módulos, Cklases, Métodos y funciones)

def despensaBarrio(unidadesDeLeche,esJubiado):
    """       
    La funcion despensaBarrio analiza el monto a pagar segun unidades que se compren y si el cliente es jubilado o no.

    Argumentos:
    unidadesDeLeche (int): la cantidad de unidades de leche que compra el cliente
    esJubiado (int): 0 si el cliente no es jubilado, cualquier otro numero si el cliente es Jubilado

    Imprime en pantalla el monto en bruto, el descuento y el monto a pagar (con los descuentos aplciados)
    La funcion retorna el descuento (int)

    >>> despensaBarrio(8,0)
    0
    >>> despensaBarrio(8,1)
    10
    >>> despensaBarrio(15,0)
    10
    >>> despensaBarrio(15,1)
    20
    >>> despensaBarrio(30,0)
    155
    >>> despensaBarrio(30,1)
    25

    """
    
    montoParcial = unidadesDeLeche * 1000
    #print(f"unidadesDeLeche {unidadesDeLeche} esJubiado {esJubiado}")
    descuento=0

    if(unidadesDeLeche <=12 and not esJubiado):
        #print("unidadesDeLeche <=12 and not esJubiado")
        montoAPagar = montoParcial        
    elif((unidadesDeLeche >12 and unidadesDeLeche <= 24) and not esJubiado):
        #print("(unidadesDeLeche >12 and unidadesDeLeche <= 24) and not esJubiado")
        montoAPagar = montoParcial * 0.9
        descuento=10
    elif(unidadesDeLeche > 24 and not esJubiado):
        #print("unidadesDeLeche > 24 and not esJubiado")
        montoAPagar = montoParcial * 0.85
        descuento=15
    if(unidadesDeLeche <=12 and esJubiado):
        #print("unidadesDeLeche <=12 and esJubiado")
        montoAPagar = montoParcial * 0.9
        descuento=10
    elif((unidadesDeLeche >12 and unidadesDeLeche <= 24) and esJubiado):
        #print("(unidadesDeLeche >12 and unidadesDeLeche <= 24) and esJubiado")
        montoAPagar = montoParcial * 0.8
        descuento=20
    elif(unidadesDeLeche > 24 and esJubiado):
        #print("unidadesDeLeche > 24 and esJubiado")
        montoAPagar = montoParcial * 0.75
        descuento=25

    #print(f"El monto sin descuento es: {montoParcial}, el descuento es del {descuento}% y el monto total a pagar es: {montoAPagar}")
    return descuento

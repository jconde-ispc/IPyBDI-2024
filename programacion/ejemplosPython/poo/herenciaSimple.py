class Vehiculo():

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "Color {}, {} ruedas".format( self.color, self.ruedas )

class Coche(Vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)        
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):        
        return super().__str__() + ", {} km/h, {} cc".format( self.velocidad,self.cilindrada )



y = Coche("azul",4,120,1500)
print(y)

"""
La herencia nos permite definir una clase que hereda todos los métodos y propiedades de otra clase.

La clase principal es la clase de la que se hereda, también llamada clase base.

La clase hija es la clase que hereda de otra clase, también llamada clase derivada.
"""
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()

  """
  Las clases secundarias heredan las propiedades y métodos de la clase principal.

En el ejemplo anterior puedes ver que la clase Car está vacía, pero hereda brand, modely move() de Vehicle.

Las clases Boat y Plane también heredan brand, model y move() de Vehicle, pero ambas anulan el método move().

Debido al polimorfismo podemos ejecutar el mismo método para todas las clases.
  """
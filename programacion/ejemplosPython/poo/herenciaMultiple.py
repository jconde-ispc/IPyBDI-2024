class A:
    def __init__(self):
        print("Soy de clase A")
    def a(self):
        print("Este método lo heredo de A")

class B:
    def __init__(self):
        print("Soy de clase B")
    def b(self):
        print("Este método lo heredo de B")

class C(B,A):
    def c(self):
        print("Este método es de C")


x = C()
x.c()
x.b()
x.a()

print(issubclass(B,C))
print(issubclass(C,B))

print(isinstance(x,B))

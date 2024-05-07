edad = int(input("Ingrese la edad"))

if edad > 18:
    print(f"La persona es mayor de edad, tiene {edad} años")
    if edad > 40:
        print(f"La persona es mayor de 40 años de edad, tiene {edad} años")
else:
    print(f"La persona es menor de edad, tiene {edad} años")
    
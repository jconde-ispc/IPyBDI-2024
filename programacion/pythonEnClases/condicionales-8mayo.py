edad = int(input("Ingrese la edad y le dire si es mayor o no: "))
mes = int(input("Ingrese el mes de 1 a 12: "))

if edad >= 18:
    print(f"Es mayor de edad, tiene {edad}")
    if(edad > 50 and mes == 5):
        print("Es mayor de 50 años y en este mes cumplis años")
else:
    print(f"Es menor de edad, tiene {edad}")

agenda = {}

while True:
    print("**" * 50)  
    print("Bienvenido a la agenda de contactos. Elija una de las siguientes opciones: ")#Diccionario (sin funciones ni POO)
    print("**" * 50)    
    print("1. Agregar una persona")
    print("2. Modificar una persona")
    print("3. Eliminar una persona")
    print("4. Mostrar toda la agenda persona a persona")
    print("5. Mostrar agenda completa")
    print("6. Salir")
    print("**" * 10)

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        apellido = input("Ingrese el apellido: ")
        nombre = input("Ingrese el nombre: ")
        dni = input("Ingrese el DNI: ")
        email = input("Ingrese el email: ")
        telefono = input("Ingrese el número de teléfono: ")

        persona = {
            "apellido": apellido,
            "nombre": nombre,
            "dni": dni,
            "email": email,
            "telefono": telefono
        }

        agenda[dni] = persona
        print("Persona agregada exitosamente.")

    elif opcion == "2":
        dni = input("Ingrese el DNI de la persona que desea modificar: ")

        if dni in agenda:
            persona = agenda[dni]
            print("Datos actuales de la persona:")
            print(persona)

            opcion_modificar = input("¿Desea cambiar los demás campos de la persona? (s/n): ")

            if opcion_modificar.lower() == "s":
                apellido = input("Ingrese el nuevo apellido: ")
                nombre = input("Ingrese el nuevo nombre: ")
                email = input("Ingrese el nuevo email: ")
                telefono = input("Ingrese el nuevo número de teléfono: ")

                persona["apellido"] = apellido
                persona["nombre"] = nombre
                persona["email"] = email
                persona["telefono"] = telefono

                print("Persona modificada exitosamente.")
            else:
                print("No se realizaron cambios.")
        else:
            print("No se encontró ninguna persona con ese DNI.")

    elif opcion == "3":
        dni = input("Ingrese el DNI de la persona que desea eliminar: ")

        if dni in agenda:
            del agenda[dni]
            print("Persona eliminada exitosamente.")
        else:
            print("No se encontró ninguna persona con ese DNI.")

    elif opcion == "4":
        if agenda:
            print("Agenda:")
            for dni, persona in agenda.items():
                print(f"DNI: {dni}")
                print(f"Apellido: {persona['apellido']}")
                print(f"Nombre: {persona['nombre']}")
                print(f"Email: {persona['email']}")
                print(f"Teléfono: {persona['telefono']}")
                print("--------------------")
        else:
            print("La agenda está vacía.")

    elif opcion == "5":
        print("La agenda completa:")
        print(agenda)

    elif opcion == "6":
        print("¡Hasta luego!")
        break

    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")
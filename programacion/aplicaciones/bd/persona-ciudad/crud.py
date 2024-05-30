import baseDeDatos
import crudPersona

def mensajeBienvenida():
    print("**" * 50)
    print("                                                                                                                ")
    print("**         BIENVENIDOS AL CRUD DE PERSONAS Y CIUDADES DONDE NACIO CADA PERSONA   ******************")
    print("                                                                                                                ")
    print("**" * 50)
    
def run():
    while True:
        
        mensajeBienvenida()

        print("Menú:")
        print("1. Insertar Persona")
        print("2. Actualizar Persona")
        print("3. Eliminar Persona")    
        print("4. Mostrar Todas las Personas")
        print("5. Mostrar Personas por Ciudad")
        print("6. Salir")
        
        opcion = input("Elija una opción: ")
        
        if opcion == "1":
            crudPersona.insertar_persona()
        elif opcion == "2":
            crudPersona.actualizar_persona()
        elif opcion == "3":
            crudPersona.eliminar_persona()    
        elif opcion == "4":
            crudPersona.mostrar_todas_las_personas()
        elif opcion == "5":
            crudPersona.mostrar_personas_por_ciudad()           
        elif opcion == "6":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

    # Cerrar cursor y conexión
    baseDeDatos.cerrarConexion()


""" Este if dice que si es ejecutado desde la terminal, entre al run
 y si es ejecutado desde otro archivo, no se ejecuta."""
if __name__ == '__main__':
  run()
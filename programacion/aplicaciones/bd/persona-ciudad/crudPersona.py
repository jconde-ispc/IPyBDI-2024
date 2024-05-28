import baseDeDatos
import crudCiudad

def insertar_persona():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    dni = input("DNI: ")
    email = input("Email: ")
    fecha_nacimiento = input("Fecha de Nacimiento (AAAA-MM-DD): ")
    telefono = input("Teléfono: ")
    ciudad_id = input("ID de la Ciudad: ")
    
    query = "INSERT INTO Persona (nombre, apellido, dni, email, fecha_nacimiento, telefono, ciudad_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (nombre, apellido, dni, email, fecha_nacimiento, telefono, ciudad_id)
    
    baseDeDatos.cursor.execute(query, values)
    baseDeDatos.conn.commit() #Es necesario realizar el commit(); de lo contrario, no se realizan cambios en la tabla 
    print("Persona insertada con éxito.")

def actualizar_persona():
    id_persona = input("ID de la Persona a actualizar: ")
    if(buscarPersona(id_persona)):
        nombre = input("Nuevo Nombre: ")
        apellido = input("Nuevo Apellido: ")
        dni = input("Nuevo DNI: ")
        email = input("Nuevo Email: ")
        fecha_nacimiento = input("Nueva Fecha de Nacimiento (AAAA-MM-DD): ")
        telefono = input("Nuevo Teléfono: ")
        ciudad_id = input("ID de Ciudad donde nacio: ")
        
        query = "UPDATE Persona SET nombre = %s, apellido = %s, dni = %s, email = %s, fecha_nacimiento = %s, telefono = %s, ciudad_id = %s WHERE id = %s"
        values = (nombre, apellido, dni, email, fecha_nacimiento, telefono, ciudad_id, id_persona)
        
        baseDeDatos.cursor.execute(query, values)
        baseDeDatos.conn.commit()
        print(f"Persona con ID {id_persona} actualizada con éxito.")
    else:
        print(f"Persona con ID {id_persona} NO EXISTE por lo tanto no puede ser modificada.")

def eliminar_persona():
    id_persona = input("ID de la Persona a eliminar: ")
    if(buscarPersona(id_persona)):
        query = "DELETE FROM Persona WHERE id = %s"
        values = (id_persona,)
        
        baseDeDatos.cursor.execute(query, values)
        baseDeDatos.conn.commit()
        print(f"Persona con ID {id_persona} eliminada con éxito.")
    else:
        print(f"Persona con ID {id_persona} NO EXISTE por lo tanto no puede ser eliminada.")

def buscarPersona(id):
    query = "SELECT * FROM Persona WHERE id = %s"
    values = (id,)
    baseDeDatos.cursor.execute(query,values)
    personaUnica = baseDeDatos.cursor.fetchone()

    print(baseDeDatos.cursor.rowcount, "Filas afectadas")

    if(baseDeDatos.cursor.rowcount == 1):
        print(personaUnica)
        return True
    else:
        print(f"No existe en la base de datos la persona con id: {id}")
        return False
    
def mostrar_todas_las_personas():
    query = "SELECT * FROM Persona"
    baseDeDatos.cursor.execute(query)
    personas = baseDeDatos.cursor.fetchall()
    
    if personas:
        for persona in personas:
            print(persona)
    else:
        print("No hay personas en la base de datos.")

def mostrar_personas_por_ciudad():
    ciudad_id = input("ID de la Ciudad para mostrar personas: ")
    
    if(crudCiudad.buscarCiudad(ciudad_id)):
        query = "SELECT * FROM Persona WHERE ciudad_id = %s"
        values = (ciudad_id,)
        baseDeDatos.cursor.execute(query, values)
        personas = baseDeDatos.cursor.fetchall()
        
        if personas:
            print(f"Las personas que nacieron en la ciudad con id:{ciudad_id} son:")
            for persona in personas:
                print(persona)
        else:
            print(f"No hay personas en la Ciudad con ID {ciudad_id}.")
    else: 
        print(f"No existe la Ciudad con ID {ciudad_id}.")


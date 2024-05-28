import baseDeDatos

def buscarCiudad(id):
    query = "SELECT * FROM Ciudad WHERE id = %s"
    values = (id,)
    baseDeDatos.cursor.execute(query,values)
    ciudadUnica = baseDeDatos.cursor.fetchone()

    print(baseDeDatos.cursor.rowcount, "Filas afectadas")

    if(baseDeDatos.cursor.rowcount == 1):
        print(ciudadUnica)
        return True
    else:
        print(f"No existe en la base de datos la ciudad con id: {id}")
        return False

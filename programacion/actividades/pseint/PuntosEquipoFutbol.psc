Algoritmo PuntosEquipoFutbol
	// Datos de entrada --
	Escribir "Ingrese la cantidad de partidos ganados del equipo"
	Leer partidosGanados
	
	Escribir "Ingrese la cantidad de partidos empatados del equipo"
	Leer pe //Es conveniente utilizar nombres que representen la información que tienen, por ejemplo: ???
	
	Escribir "Ingrese la cantidad de partidos perdidos del equipo"
	Leer partidosPerdidos
	
	//Calculos necesarios para llegar al resultado
	puntosEquipo = (partidosGanados * 3) + (pe * 1) + (partidosPerdidos * 0)
	
	//Resultado
	Escribir "El equipo tiene ",puntosEquipo, " puntos hasta el momento, luego de jugar ",partidosGanados+pe+partidosPerdidos, " partidos"
	
FinAlgoritmo

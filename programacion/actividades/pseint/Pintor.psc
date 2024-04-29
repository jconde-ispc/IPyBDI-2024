Algoritmo Pintor
	//	Datos de entrada
	Escribir "Ingrese el alto de la pared"
	Leer altoPared
	Escribir "Ingrese el ancho de la pared"
	Leer anchoPared
	Escribir "Ingrese el costo del metro cuadrado que cobra el pintor"
	Leer costoPintorPorM2
	// Cálculos necesarios para lograr el resultado
	superficiePared = altoPared * anchoPared
	Escribir "El galpon tiene un anche de", anchoPared, " metros y un alto de ", altoPared, " metros"
	Escribir "Esto hace que la superficie del galpon sea de ",superficiePared, " metros cuadrados"
	
	// Resultado
	costoManoObra = superficiePared * costoPintorPorM2
	Escribir "El costo de mano de obra del pintor para pintar el galpón es de ",costoManoObra
	
	
FinAlgoritmo

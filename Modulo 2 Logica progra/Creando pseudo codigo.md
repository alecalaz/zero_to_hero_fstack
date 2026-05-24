1.
Definir `horas trabajadas`
Definir `tarifa por hora`
Definir `salario`
#Cuantas horas ha trabajado?
Pedir `horas trabajadas`
Pedir `tarifa por hora`
salario = horas trabajadas * tarifa por hora
mostrar salario

2.
Definir `cantidad de notas`
Definir `contador` 
Definir `nota`
Definir `cantidad_aprobadas`
Definir `cantidad_reprobadas`
Definir promedio total
Definir promedio aprobadas
Definir promedio reprobadas
Mostrar "Ingrese su cantidad de notas"
Pedir `cantidad de notas`
`contador` = 1
Mientras que (`contador` < cantidad) hacer:
	Mostar "Ingrese la nota numero"
	 Mostrar `contador`
	 Pedir `nota`
	`contador` = `contador` + 1
	Si `nota` >= 70:
		cantidad_aprobadas = 0
		cantidad_aprobadas  = cantidad_aprobadas + 1
	 Sino `nota` <= 70:
		 cantidad_reprobadas = 0
		 cantidad_reprobadas = cantidad_reprobadas + 1



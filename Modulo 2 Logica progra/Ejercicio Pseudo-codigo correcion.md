Hola Alejandro, va muy bien, solo quedan un par de detalles por afinar:

1. Descuento del producto  
La idea está bien, pero el cálculo no es correcto.  
Actualmente está haciendo:  
  
precio * 0.02 o precio * 0.1  
Eso calcula solo el descuento, no el precio final.  
  
Debe calcular:  
descuento  
luego restarlo al precio original  
  
Además, no es necesario sobrescribir la misma variable para todo.  
  
2. Tiempo en segundos  
Va bien encaminado, pero hay varios detalles:  
  
Está restando al revés:  
tiempo_segundos = tiempo_segundos - 10_minutos  
debería calcular cuánto falta, no cuánto sobra.  
  
Hay un error de nombre:  
tiempo_segundo  
(falta la “s”)  
  
No es necesario asignar "Mayor" a la variable, solo mostrar el mensaje.  
  
3. Suma de 1 hasta N  
  
No se necesita una lista del 1 al 100  
  
La suma no es:  
numero_usuario + cada numero en lista  
  
Se necesita un ciclo que vaya acumulando desde 1 hasta el número ingresado
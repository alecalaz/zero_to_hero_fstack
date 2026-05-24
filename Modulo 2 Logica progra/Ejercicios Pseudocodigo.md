1.
Cree un pseudocódigo que le pida un `precio de producto` al usuario, calcule su descuento y muestre el precio final tomando en cuenta que:

- Si el precio es menor a 100, el descuento es del 2%.
    

- Si el precio es mayor o igual a 100, el descuento es del 10%.
    

- Ejemplos:
    
    - 120 → 108
        
    
    - 40 → 39.2
//Trabajo
Definir `descuento`
`precio_del_producto` = Mostrar "Ingrese el precio del producto"
Si entonces `precio_del_producto` < 100:
	`descuento` = `precio_del_producto` * 0.02
	 `precio_del_producto` = `precio_del_producto` - `descuento`
Sino `precio_del_producto` >= 100:
	`descuento` = `precio_del_producto` * 0.1
	`precio_del_producto` = `precio_del_producto` - `descuento`
Mostrar "El precio con descuento es de `precio_del_producto`"
Fin

2.
	Cree un pseudocódigo que le pida un `tiempo en segundos` al usuario y calcule si es menor o mayor a 10 minutos. Si es menor, muestre cuantos segundos faltarían para llegar a 10 minutos. Si es mayor, muestre “Mayor”. Si es exactamente igual, muestre “Igual”.

- Ejemplos:
    
    - 1040 → Mayor
        
    
    - 140 → 460
        
    
    - 600 → Igual
        
    
    - 599 → 1
//trabajo

`tiempo_segundos` = Mostrar "Ingrese su tiempo en segundos"
`10_minutos` = 600
Si entonces `tiempo_segundos` < `10_minutos`:
	`tiempo_segundos` = `10_minutos` - `tiempo_segundos`
	 Mostrar "Para 10 minutos faltan `tiempo_segundos`"
Sino `tiempo_segundos` > `10_minutos`:
	 Mostrar "Mayor"
Sino `tiempo_segundos` == `10_minutos`:
	 Mostrar "Igual"
Fin

3.
Cree un algoritmo que le pida un numero al usuario, y realice una suma de cada numero del 1 hasta ese número ingresado. Luego muestre el resultado de la suma.

- 5 → 15 (1 + 2 + 3 + 4 + 5)
    

- 3 → 6 (1 + 2 + 3)
    

- 12 → 78 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12)
//trabajo

`numero_usuario` = 0
`contador` = 1
Pedir `numero_usuario` = Mostrar "Elija un numero del 1 al 100"
Mientras que `contador` <= `numero_usuario`:
	`suma` = `suma` + `contador`
	`contador` = `contador` + 1
Fin mientras

Mostrar "El resultado de la suma es `suma`"


Fin
	




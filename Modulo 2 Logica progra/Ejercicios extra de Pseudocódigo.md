1.
Cree un algoritmo que le pida 2 números al usuario, los guarde en dos variables distintas (`primero` y `segundo`) y los ordene de menor a mayor en dichas variables.

- Ejemplos:
    
    - A: 56, B: 32 → A: 32, B: 56
        
    
    - A: 24, B: 76 → A: 24, B: 76
        
    
    - A: 45, B: 12 → A: 12, B: 45

//trabajo
`primero` = 0
`segundo` = 0
definir `primero`
pedir mostrar "Ingrese el primer numero"

definir `segundo`
pedir mostrar "Ingrese el segundo numero"

si entonces `primero` < `segundo`:
	mostrar "`primero` `segundo` "
sino `segundo` < `primero`:
	mostrar "`segundo` `primero` "
Fin

2.
Cree un algoritmo que le pida al usuario una velocidad en km/h y la convierta a m/s. Recuerda que `1 km == 1000m` y `1 hora == 60 minutos * 60 segundos`.

- Ejemplos:
    
    - 73 → 20.27
        
    
    - 50 → 13.88
        
    
    - 120 → 33.33

//trabajo
`1_km` = 1000
`1_hora` = 3600
`velocidad` = 0

Inicio
Definir `velocidad`
Mostrar "Ingrese su velocidad en km/h"

`velocidad_a_ms` = `velocidad` * `1_km` // `1_hora`

Mostrar "Su velocidad en m/s es de `velocidad_a_ms`"
Fin

3.
Cree un algoritmo que le pregunte al usuario por el sexo de 6 personas, ingresando 1 si es mujer o 2 si es hombre, y muestre al final el porcentaje de mujeres y hombres.

- Ejemplos:
    
    - 1, 1, 1, 2, 2, 2 → 50% mujeres y 50% hombres
        
    
    - 1, 1, 2, 2, 2, 2 → 33.3% mujeres y 66.6% hombres
        
    
    - 1, 1, 1, 1, 1, 2 → 83.3% mujeres y 16.6% hombres
//trabajo
Definir
`numero_mujeres` = 0
`numero_hombres` = 0
`sexo` = 0
Mostrar "Ingrese el sexo de 6 personas donde 1 es mujer y 2 hombre"

Si entonces `sexo` == 1:
	`numero_mujeres` = `numero_mujeres` + 1
Sino `sexo` == 2:
	`numero_hombres` = `numero_hombres + 1 

`Porcentaje_mujeres` = `numero_mujeres` // 6  
`Porcentaje_hombres` = `numero_hombres`  // 6

Mostrar "`Porcentaje_mujeres` y `Porcentaje_hombres`"

Fin
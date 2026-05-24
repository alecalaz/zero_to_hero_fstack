1. Paso 7: Hora del sistema

Este paso no está incluido en el documento. Necesita agregar un comando que muestre la hora del sistema operativo desde la terminal, junto con su captura de pantalla. Le recomendamos investigar qué comando permite ver la hora actual en CMD o PowerShell de Windows.

![[Pasted image 20260428181204.png]]

2. Paso 6: Aplicación abierta manualmente

El enunciado pide abrir primero una aplicación sencilla (como la Calculadora o el Bloc de notas), luego localizar su PID en la lista de procesos y finalmente terminarla. Falta mostrar esa aplicación abierta y la identificación de su PID antes de ejecutar 'taskkill'. Con terminar 'claude.exe' se entiende la idea, pero sería ideal mostrar el flujo completo desde la apertura.

Abrir calculadora
![[Pasted image 20260428181429.png]]

Terminar proceso
![[Pasted image 20260428181620.png]]

3. Paso 8: Nombre del archivo

Los archivos quedaron como 'welcome1.txt', 'welcome2.txt' y 'welcome3.txt', pero el enunciado indica que todos deben llamarse 'welcome.txt'. Renombre cada uno usando el comando 'ren' para que el nombre final sea exactamente 'welcome.txt' en cada carpeta.

C:\Users\Lenovo\Desktop\Proyectos>cd..

C:\Users\Lenovo\Desktop>mkdir Empleado1, Empleado2, Empleado3

C:\Users\Lenovo\Desktop>mkdir Empleado

C:\Users\Lenovo\Desktop>ren Empleado Empleados

C:\Users\Lenovo\Desktop>cd Empleado1

C:\Users\Lenovo\Desktop\Empleado1>echo > bienvenida1.txt

C:\Users\Lenovo\Desktop\Empleado1>cd..

C:\Users\Lenovo\Desktop>cd Empleado2

C:\Users\Lenovo\Desktop\Empleado2>echo > bienvenida2.txt

C:\Users\Lenovo\Desktop\Empleado2>cd..

C:\Users\Lenovo\Desktop>cd Empleado3

C:\Users\Lenovo\Desktop\Empleado3>echo > bienvenida3.txt

C:\Users\Lenovo\Desktop\Empleado3>cd..

C:\Users\Lenovo\Desktop>move Empleado1 c:\Users\Lenovo\Desktop\Empleados
Se ha(n) movido         1 directorio(s).

C:\Users\Lenovo\Desktop>move Empleado2 c:\Users\Lenovo\Desktop\Empleados
Se ha(n) movido         1 directorio(s).

C:\Users\Lenovo\Desktop>move Empleado3 c:\Users\Lenovo\Desktop\Empleados
Se ha(n) movido         1 directorio(s).

C:\Users\Lenovo\Desktop>cd Empleados\Empleado1

C:\Users\Lenovo\Desktop\Empleados\Empleado1>ren bienvenida1.txt welcome.txt

C:\Users\Lenovo\Desktop\Empleados\Empleado1>cd Empleados\Empleado2
El sistema no puede encontrar la ruta especificada.

C:\Users\Lenovo\Desktop\Empleados\Empleado1>cd..

C:\Users\Lenovo\Desktop\Empleados>cd Empleado2

C:\Users\Lenovo\Desktop\Empleados\Empleado2>ren bienvenida2.txt welcome.txt

C:\Users\Lenovo\Desktop\Empleados\Empleado2>cd..

C:\Users\Lenovo\Desktop\Empleados>cd Empleado3

C:\Users\Lenovo\Desktop\Empleados\Empleado3>ren bienvenida3.txt welcome.txt

C:\Users\Lenovo\Desktop\Empleados\Empleado3>
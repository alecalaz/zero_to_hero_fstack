---
Es:
---
--Estructura--
## Estructura del Proyecto 🗂️

Deberá dividir el proyecto en los siguientes módulos:

- `main`: tendrá el punto de entrada del programa.
    

- `menu`: tendrá toda la lógica relacionada al menú de opciones.
    

- `actions`: tendrá toda la lógica de las acciones del menú, excepto las de exportar e importar datos.
    

- `data`: tendrá toda la lógica de exportación e importación de datos.



---Primer paso--- 
==Menu==
==Interfaz de comando. Prints e inputs.==
==Mensaje de bienvenida==
data
main

==Envovler en try/except para opcion valida del menu==

---Paso 2----
==Solicitar informacion del estudiante==
==Inputs==
==Opciones validas==
==notas de 0 a 100. try except por si hay valor menor a 0 o mayor a 100==
- Nombre completo
    

- Sección (ejemplo: `11B`)
    

- Nota de español
    

- Nota de inglés
    

- Nota de sociales
    

- Nota de ciencias

---Tercer paso---
Opcion para ver todos los estudiantes ingresados
Crear funcion manejo archivos en csv/json

---Cuarto paso---
Funcion para sacar top 3 estudiantes y promedio de notas de cada estudiante

---Quinto paso---
Funcion para exportar todos los datos a un csv
importar datos y validar si ya existe uno, si no, informar al usuario
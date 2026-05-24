1. El archivo JSON inicial (`pokemon.json`)

Supongamos que tu archivo tiene esta estructura básica:

```
{
    "nombre": "Pikachu",
    "tipo": "Eléctrico",
    "nivel": 25
}
```

2. Programa en Python para leer, actualizar y guardar

Usaremos la librería `json` integrada y las funciones de manejo de archivos que hemos discutido.

```
import json

nombre_archivo = 'pokemon.json'

try:
    # PASO 1: Leer el archivo existente (Deserialización)
    # Abrimos el archivo en modo lectura ('r') [7, 9]
    with open(nombre_archivo, 'r') as fhand:
        datos_string = fhand.read() # Leemos el contenido como cadena [10]
        pokemon = json.loads(datos_string) # Convertimos a diccionario de Python [6, 11]
    
    print(f"Datos actuales del Pokémon: {pokemon}")

    # PASO 2: Pedir nueva información al usuario
    # Usamos input() para capturar datos [12, 13]
    nueva_habilidad = input("Introduce una nueva habilidad para el Pokémon: ")
    nuevo_nivel = input("¿A qué nivel subió?: ")

    # PASO 3: Agregar la información al objeto de Python
    # Los objetos JSON se manipulan como diccionarios estándar [14, 15]
    pokemon['habilidad'] = nueva_habilidad
    pokemon['nivel'] = int(nuevo_nivel) # Convertimos el input a entero [16, 17]

    # PASO 4: Guardar la información actualizada (Serialización)
    # Abrimos en modo escritura ('w') para truncar y sobreescribir [7, 9]
    with open(nombre_archivo, 'w') as fhand:
        # Convertimos el diccionario a texto JSON legible [18, 19]
        # indent=4 es una mejor práctica para que sea fácil de leer por humanos
        json_actualizado = json.dumps(pokemon, indent=4)
        fhand.write(json_actualizado)

    print("¡Archivo actualizado exitosamente!")

except FileNotFoundError:
    print(f"Error: El archivo {nombre_archivo} no existe.") # Patrón guardián [20, 21]
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
```

Notas técnicas y mejores prácticas de Senior Dev:

- **Mapeo Natural:** Recuerda que al usar `json.loads()`, los objetos `{ }` de JSON se convierten automáticamente en **diccionarios** de Python, lo que te permite usar la sintaxis `pokemon['clave'] = valor` para agregar o actualizar datos de forma inmediata.
- **Modo de Apertura:** Para guardar los cambios en el mismo archivo, usamos el modo `'w'` en la función `open()`. Esto borrará el contenido viejo y escribirá el nuevo diccionario completo ya actualizado.
- **Gestión de Tipos:** Los datos que vienen de `input()` siempre son cadenas de texto (**strings**). Si planeas hacer cálculos con el nivel del Pokémon más adelante, asegúrate de convertirlo usando `int()` antes de guardarlo.
- **Seguridad y Errores:** Siempre envuelve la apertura del archivo en un bloque **try/except**. Es muy común que el archivo no se encuentre o que el formato JSON esté "roto" (mal formado), y no queremos que el programa "explote" frente al usuario.
- **Codificación:** Si tu Pokémon tiene nombres con caracteres especiales (como acentos o eñes), Python 3 manejará esto internamente como **Unicode**, lo cual es una gran ventaja sobre versiones antiguas
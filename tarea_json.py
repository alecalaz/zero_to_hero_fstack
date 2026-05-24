import json


with open("pokemon.json", "r", encoding="utf-8") as archivo:
    pokemones = json.load(archivo)

print(f"Se cargaron {len(pokemones)} Pokémon(es) del archivo.")

print("Ingresa los datos del nuevo Pokémon: ")

name = input("Nombre: ")
type = input("Tipo (ej: Fire, Water, Grass): ")
level = int(input("Nivel: "))
weight_kg = float(input("Peso en kg (ej: 6.5): "))

shiny_input = input("¿Es shiny? (s/n): ").lower()
if shiny_input == 's':
    shiny_input == True
else:
    shiny_input == False
held_item = input("Item que lleva (Enter si no lleva nada): ")


skills_input = input("Habilidades separadas por coma (ej: Ember,Scratch): ")
skills = [s.strip() for s in skills_input.split(",")]


print("\n--- Stats ---")
stats = {
    "hp":         int(input("HP: ")),
    "attack":     int(input("Attack: ")),
    "defense":    int(input("Defense: ")),
    "sp_attack":  int(input("Sp. Attack: ")),
    "sp_defense": int(input("Sp. Defense: ")),
    "speed":      int(input("Speed: ")),
}

#busque para armar la estructura en jason, basimanete un diccionario con los valores declarados en los inputs de arriba
nuevo_pokemon = {
    "name":      name,
    "type":      type,
    "level":     level,
    "weight_kg": weight_kg,
    "is_shiny":  shiny_input,
    "held_item": held_item,
    "skills":    skills,
    "stats":     stats,
}

#variable declarada arriba que son los pokemones del json
pokemones.append(nuevo_pokemon)

#'w' para el modo write
with open("pokemon.json", "w", encoding="utf-8") as archivo:
    json.dump(pokemones, archivo, indent=3)



import json

def read_pokemon_data(json_file):
    with open(json_file, "r", encoding="utf-8") as archivo:
        pokemones = json.load(archivo)

    print(f"Se cargaron {len(pokemones)} Pokémon(es) del archivo.")
    return pokemones


def ask_pokemon_data():
    print("Ingresa los datos del nuevo Pokémon: ")

    is_shiny_input = input("¿Es shiny? (s/n): ").lower()
    skills_input = input("Habilidades separadas por coma (Ember, Scratch): ")

    return {
        "name":       input("Nombre: "),
        "type":       input("Tipo: "),
        "level":      int(input("Nivel: ")),
        "weight_kg":  float(input("Peso en kg: ")),
        "is_shiny":   True if is_shiny_input == 's' else False, #no sabia que se podia hacer un condicional en una sola linea :) me facilito las cosas!
        "held_item":  input("Item que lleva: "),
        "skills":     [s.strip() for s in skills_input.split(",")],
        "stats": {
            "hp":         int(input("HP: ")),
            "attack":     int(input("Attack: ")),
            "defense":    int(input("Defense: ")),
            "sp_attack":  int(input("Sp. Attack: ")),
            "sp_defense": int(input("Sp. Defense: ")),
            "speed":      int(input("Speed: ")),
        }
    }


def build_pokemon_dict(data):
    return {
        "name":      data["name"],
        "type":      data["type"],
        "level":     data["level"],
        "weight_kg": data["weight_kg"],
        "is_shiny":  data["is_shiny"],
        "held_item": data["held_item"],
        "skills":    data["skills"],
        "stats":     data["stats"]
    }



def write_pokemon_data(input_path, data):
#'w' para el modo write
    with open(input_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=3)

def main():
    pokemones = read_pokemon_data("pokemon.json")
    datos = ask_pokemon_data()
    pokemones.append(build_pokemon_dict(datos))
    write_pokemon_data("pokemon.json", pokemones)

if __name__ == "__main__":
    main()
import csv

def game_info(file_path, data):
    with open(file_path, 'w', encoding='utf-8', newline='') as file:
        headers = data[0].keys()

        writer = csv.DictWriter(file, fieldnames=headers)

        # Escribimos la primera fila en el documento con los títulos
        writer.writeheader()

        # Insertamos la lista completa de nuestros videojuegos
        writer.writerows(data)


def game_info_tabs(file_path, data):
    with open(file_path, 'w', encoding='utf-8', newline='') as file:
        headers = data[0].keys()

        writer = csv.DictWriter(file, fieldnames=headers, delimiter='\t')

        writer.writeheader()
        writer.writerows(data)


# pedir al usuario cuantos juegos quiere registrar
cantidad = int(input("¿Cuántos videojuegos quieres registrar? "))

# crear lista vacia e iterar por el rango de veces ingresado en cantidad
video_games = []
for i in range(cantidad):
    print(f"\nVideojuego {i + 1}:")
    nombre = input("  Nombre: ")
    genero = input("  Género: ")
    desarrollador = input("  Desarrollador: ")
    clasificacion = input("  Clasificación: ")

    # Guardamos cada juego como diccionario y lo agregamos a la lista
    juego = {
        'nombre': nombre,
        'genero': genero,
        'desarrollador': desarrollador,
        'clasificacion': clasificacion
    }
    video_games.append(juego)

# CSV separado por comas
game_info('video_games.csv', video_games)

# CSV separado por tabulaciones
game_info_tabs('video_games_tabs.csv', video_games)

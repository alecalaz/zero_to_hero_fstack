# import os

# with open('quijote.txt', "r") as file:
#     content = file.read()
#     print(content)



# def read_complete_file(path):
#     # Usamos 'with' para un manejo seguro del archivo
#     with open(path, 'r', encoding='utf-8') as file:
#         content = file.read()
#         print(content)

# read_complete_file('quijote.txt')


def read_file_by_lines(path):
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

        # Iteramos sobre la lista de líneas obtenida
        for number, line in enumerate(lines, start=1):
            # Usamos strip() para remover los saltos de línea y limpiar espacios
            print(f"Line {number}: {line.strip()}")

read_file_by_lines('archivos.csv')
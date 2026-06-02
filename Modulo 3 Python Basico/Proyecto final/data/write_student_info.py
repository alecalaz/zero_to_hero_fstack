# tendrá toda la lógica de exportación e importación de datos.

import json
import actions.student_info

def write_student_info(input_data, dest_file):
    with open(dest_file, "w", encoding="utf-8") as file:
        json.dump(input_data, file, indent=3)

write_student_info(actions.student_info(), 'all_student_info.json')


def read_all_students(file_path):
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            students = json.load(file)
            print(f"Se cargaron {len(students)} estudiantes del archivo.")
            return students
    except FileNotFoundError as ex:
        print(f'No es encontro el archivo especificado {ex}')








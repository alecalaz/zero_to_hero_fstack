# tendrá toda la lógica de exportación e importación de datos.
from actions.student_info import Student
import json
import csv


def write_student_info(input_data, dest_file):
    """Escribe informacion del estudiante a archivo json"""
    with open(dest_file, "w", encoding="utf-8") as file:
        json.dump(input_data, file, indent=3)


def read_all_students(file_path):
    """Carga todos los estudiantes de un archivo json"""
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            students = json.load(file)
            print(f"Se cargaron {len(students)} estudiantes del archivo.")
            return students
    except FileNotFoundError as ex:
        print(f'No es encontro el archivo especificado {ex}')


def export_student_info(student_list, output_file):
    """Exporta archivo csv"""
    dict_list = [vars(student) for student in student_list]
    with open(output_file, 'w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=dict_list[0].keys(), delimiter='\t')
        writer.writeheader()
        writer.writerows(dict_list)


def import_student_csv(file_csv):
    """Importa informacion de csv a un csv existente"""
    try:
        with open(file_csv, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter='\t')
            list_of_students = []
            for student in reader:
                spanish = int(student['spanish_grade'])
                english = int(student['english_grade'])
                civic = int(student['civic_grade'])
                science = int(student['science_grade'])
                
                list_of_students.append(Student(student['full_name'], student['section'], spanish, english, civic, science))
            return list_of_students
    except FileNotFoundError as ex:
        print(f'No se encontro el archivo{ex}')
        









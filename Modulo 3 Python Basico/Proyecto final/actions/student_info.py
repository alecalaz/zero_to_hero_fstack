#Tendrá toda la lógica de las acciones del menú, excepto las de exportar e importar datos.
import json

def student_info():
    student_list_info = []
    students_quantity = range(int(input('Cuantos estudiantes desea ingresar?: ')))


    for student in students_quantity:
        while True:
            try:
                full_name = input('Ingrese nombre completo: ')
                if full_name.isdigit():
                    raise ValueError('El nombre no pude ser un numero!')
                break
            except ValueError as ex:
                    print(ex)
        while True:
            try:
                section = input('Ingrese numero de seccion(Ejemplo 11A): ')
                if section.isdigit():
                    raise ValueError('Ingrese la seccion la letra. Ej 11 A')
                break
            except ValueError as ex:
                print(ex)
        while True:
            try:
                    spanish_note = int(input('Nota de español: '))
                    if spanish_note < 0 or spanish_note > 100:
                        raise ValueError('La nota debe ser entr 0 y 100!')
                    break
            except ValueError as ex:
                    print(ex)
        while True:
                try:
                    english_note = int(input('Nota de ingles: '))
                    if english_note < 0 or english_note > 100:
                        raise ValueError('La nota debe ser entr 0 y 100!')
                    break
                except ValueError as ex:
                    print(ex)
        while True:
                try:
                    civic_note = int(input('Nota estudios sociales: '))
                    if civic_note < 0 or civic_note > 100:
                        raise ValueError('La nota debe ser entr 0 y 100!')
                    break
                except ValueError as ex:
                    print(ex)
        while True:
            try:
                science_note = int(input('Nota de ciencias: '))
                if science_note < 0 or science_note > 100:
                    raise ValueError('La nota debe ser entr 0 y 100!')
                break
            except ValueError as error:
                    print(error)
        student_data = {
            'full name': full_name,
            'section': section,
            'spanish_grade': spanish_note,
            'english_grade': english_note,
            'civic_grade': civic_note,
            'science_grade': science_note
        }
        student_list_info.append(student_data)

    return student_list_info




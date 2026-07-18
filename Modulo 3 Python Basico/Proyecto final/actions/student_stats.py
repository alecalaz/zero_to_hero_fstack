

def student_average(student):

    total = student['spanish_grade'] + student['english_grade'] + student['civic_grade'] + student['science_grade']
    average = total / 4
    return average


def top_3_students(student_list):
    top_3 = []
    for student in student_list:
        student_avrg = student_average(student)
        top_3.append((student_avrg, student))
    top_3.sort(reverse=True)
    return top_3[:3]
    

def all_student_average(all_students_list):
    all_avrg = 0
    for student in all_students_list:
        all_avrg += student_average(student)
    avrg = all_avrg / len(all_students_list)
    return avrg


# test_students = [
#     {'full name': 'Ana Lopez', 'Section': '11A', 'spanish_grade': 90, 'english_grade': 85, 'civic_grade': 88, 'science_grade': 92},
#     {'full name': 'Carlos Ruiz', 'Section': '11B', 'spanish_grade': 70, 'english_grade': 65, 'civic_grade': 72, 'science_grade': 68},
#     {'full name': 'Maria Gomez', 'Section': '11A', 'spanish_grade': 95, 'english_grade': 98, 'civic_grade': 91, 'science_grade': 97},
#     {'full name': 'Pedro Diaz', 'Section': '11C', 'spanish_grade': 60, 'english_grade': 55, 'civic_grade': 58, 'science_grade': 62},
#     {'full name': 'Ana Lopez', 'section': '11A', 'spanish_grade': 90, 'english_grade': 85, 'civic_grade': 88, 'science_grade': 92},
#     {'full name': 'Carlos Ruiz', 'section': '11B', 'spanish_grade': 70, 'english_grade': 65, 'civic_grade': 72, 'science_grade': 68},
#     {'full name': 'Maria Gomez', 'section': '11A', 'spanish_grade': 95, 'english_grade': 98, 'civic_grade': 91, 'science_grade': 97},
#     {'full name': 'Pedro Diaz', 'section': '11C', 'spanish_grade': 60, 'english_grade': 55, 'civic_grade': 58, 'science_grade': 62},
# ]

# print(all_student_average(test_students))

def return_all_students_info(all_students_list):
    for student in all_students_list:
        print(f"Nombre: {student['full_name']}, Sección: {student['section']}, Nota Promedio: {student_average(student)}")




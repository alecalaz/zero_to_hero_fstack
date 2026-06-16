

def student_average(student):

    total = student.spanish_grade + student.english_grade + student.civic_grade + student.science_grade
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


def return_all_students_info(all_students_list):
    for student in all_students_list:
        print(f"Nombre: {student.full_name}, Sección: {student.section}, Nota Promedio: {student_average(student)}")




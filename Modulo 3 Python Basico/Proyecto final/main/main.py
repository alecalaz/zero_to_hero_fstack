#tendrá el punto de entrada del programa.

from menu.main_menu import main_menu
from actions.student_stats import return_all_students_info, top_3_students, all_student_average, student_average
from actions.student_info import student_info
from data.write_student_info import write_student_info, read_all_students, export_student_info, import_student_csv
def main():
    student_list = []
    while True:
        option = main_menu()
        if option == 1:
            student = student_info()
            student_list.extend(student)
        elif option == 2:
            return_all_students_info(student_list)
        elif option == 3:
            print(top_3_students(student_list))
        elif option == 4:
            print(all_student_average(student_list))
        else:
            export_student_info(student_list, output_file='students.csv')


if __name__ == '__main__':
    main()




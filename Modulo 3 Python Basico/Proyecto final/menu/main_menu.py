#tendrá toda la lógica relacionada al menú de opciones.

def main_menu():
    print('''---Bienvenido al Insituto de Estudios Generales de Lyfter---
        Por favor digite una opcion del menu:          
        ''')
    counter = 0
    try:
        print('''
            1: Ingresar nuevos estudiantes al sistema
            2: Ver informacion de todos los estudiantes ingresados
            3: Ver top 3 estudiantes con la mejor nota promedio
            4: Ver nota promedio de todos los estudiantes
            5: Exportar los datos actuales a un csv
            ''')
        user_selection = int(input('Selecione una opcion: '))
        if user_selection < 1 or user_selection > 5:
            raise ValueError(f"Opción '{user_selection}' no válida. Ingrese un número entre 1 y 5.")
        return user_selection
    except ValueError as error:
        print(f'Error: {error}')
        
    # #while counter < student_quantity:

main_menu()
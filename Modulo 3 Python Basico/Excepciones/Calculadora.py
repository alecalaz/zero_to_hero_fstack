constant_number = 10


def sum_function(num):
    global constant_number
    total_sum = constant_number + num
    constant_number = total_sum
    return total_sum


def min_function(num):
    global constant_number
    total_min = constant_number - num
    constant_number = total_min
    return total_min


def multiply_function(num):
    global constant_number
    total_multi = constant_number * num
    constant_number = total_multi
    return total_multi


def divide_function(num):
    global constant_number
    try:
        if constant_number / num:
            raise ValueError()
        else:
            total_division = constant_number / num
            constant_number = total_division
            return total_division
    except ZeroDivisionError as e:
        print(f'No se puede dividir entre 0!')


def clean_result(num):
    global constant_number
    if num == 5:
        constant_number = 0
        print(f'Resultado borrado. Volviendo al menu principal. El valor vuelva {constant_number}')

#paso 2 conseguir la opcion y en base a la opcion llamar a la funcion indicada
def get_option():
        try:
            math_option = int(input(
            f"""
        Numero actual es {constant_number}
        Elija una opcion matematica escribiendo el numero:
        1. Suma
        2. Resta
        3. Multiplicacion
        4. Division
        5. Borrar resultado

        """
))
        except Exception as ex:
            print(f'El numero tiene que ser digitado {ex}')

        
        return math_option

#paso 1 presentar el menu al usuario
def main_calc():
    try:
        option = get_option()
        if option == 1:
            num = int(input(f'Ingrese el numero que desea sumar a {constant_number}: '))
            print(sum_function(num))
        elif option == 2:
            num = int(input(f'Ingrese el numero que desea restar a {constant_number}: '))
            print(min_function(num))
        elif option == 3:
            num = int(input(f'Ingrese el numero que desea multiplicar por {constant_number}: '))
            print(multiply_function(num))
        elif option == 4:
            num = int(input(f'Ingrese el numero que desea dividirle a {constant_number}: '))
            print(divide_function(num))
        elif option == 5:
            clean_result(5)
        else:
            print(f'Por favor ingresa una opcion del 1 al 5')
            

    except Exception as ex:
        print(f'Por favor digite el numero, no escriba')

while True:
    main_calc()






#funciones deben ser ordenadas
def function_1():
	print('Ejecutando 1')


def function_2():
	print('Ejecutando 2')


def function_3():
	print('Ejecutando 3')


def main():
	function_1()
	function_2()
	function_3()


main()

#parametros de funciones
def print_parameters(parameter_1, parameter_2, parameter_3):
	print(f'This is parameter 1: {parameter_1}')
	print(f'This is parameter 2: {parameter_2}')
	print(f'This is parameter 3: {parameter_3}')


print_parameters(50, 'Hello', True)

#parametros pueden tener valores predefinidos
def print_parameters(parameter_1, parameter_2='Default value', parameter_3=100):
    print(f'This is parameter 1: {parameter_1}')
    print(f'This is parameter 2: {parameter_2}')
    print(f'This is parameter 3: {parameter_3}')
print_parameters(50)

#print de la funcion
def get_max_of_two_numbers(number1, number2):
  if number1 > number2:
    return number1

  return number2


print(get_max_of_two_numbers(3, 7))
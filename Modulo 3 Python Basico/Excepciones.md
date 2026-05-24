errores que suceden con sintaxis valida

Siempre estar a la defensiva de las acciones y errores del usuario:

def main():
	my_second_string = 'Hello'

	try:
		my_second_int = int(my_second_string)
	except ValueError:
		print('Hubo un error al convertir este string a numero!')
  print(my_second_int + 2)


if __name__ == '__main__':
	main()

output
'Hubo un error al convertir este string a numero!'


varios except:

def main():
	my_list = [
	  '2',
	  'Hello'
	]
	index_to_use = 1
	
	try:
	  list_element_to_convert = my_list[index_to_use]
	  element_to_int = int(list_element_to_convert)
	  print(element_to_int)
	except IndexError as error:
	  print(f'El indice a usar no existe en la lista. Error: {error}')
	except ValueError as error:
	  print(f'El elemento de la lista no es un numero valido. Error: {error}')


if __name__ == '__main__':
	main()


Si no sabemos cual exception vamos a percibir 'Exception' atrapa cualquier tipo de exception

def main():
	my_list = [
	  '2',
	  'Hello'
	]
	index_to_use = 1
	
	try:
	  list_element_to_convert = my_list[index_to_use]
	  element_to_int = int(list_element_to_convert)
	  print(element_to_int)
	except Exception as error:
	  print(f'Ha ocurrido un error: {error}')


if __name__ == '__main__':
	main()


`BaseException`

- `Exception`
    
    `ValueError`: Cuando un argumento tiene el tipo correcto, pero un valor inapropiado
        
    
    `TypeError`: Cuando se realiza una operación con un tipo de dato incorrecto
        
    
    `KeyError`: Al intentar acceder a una clave inexistente en un diccionario
        
    
    `IndexError`: Cuando se intenta acceder a un índice fuera del rango de una lista.

	`AttributeError`: Cuando un objeto no tiene un atributo solicitado.
	`ZeroDivisionError`: Cuando se intenta dividir un número por cero.


def main():
	my_list = [
	  '2',
	  'Hello'
	]
	index_to_use = 1
	
	try:
	  list_element_to_convert = my_list[index_to_use]
	  element_to_int = int(list_element_to_convert)
	  print(element_to_int)
	except Exception as error:
	  print(f'Ha ocurrido un error: {error}')


if __name__ == '__main__':
	main()



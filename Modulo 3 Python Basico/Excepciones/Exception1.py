def ask_name():
        name = input('Ingrese su nombre: ')
        if name.isdigit():
            raise ValueError('El nombre no puede ser un numero!')
        return name


def ask_age():
      age = int(input('Ingrese su edad: '))
      if age < 0:
            raise ValueError('La edad no puede ser menor a 0')
      elif age > 100:
            raise ValueError('La edad no puede ser mayor a 100')
      return age

try:
    name = ask_name()
    age = ask_age()
    print(f'Hola {name}, su edad es de {age}')

except ValueError as e:
      print(f'Error: {e}')


def convert_to_int(list):
      converted_list = []
      for char in list:
            try:
                int(char)
                converted_list.append(char)
                print(f'{char} convertido a {int(char)}')
            except ValueError as e:
                  print(f'No se pudo convertir el elemento {char}')
      return converted_list

            
my_list = ['4', 'hola', '10', '5.2']
print(convert_to_int(my_list))


def sumar_valores(list):
      count = 0
      for i in list:
            try:
                count += float(i)
                print(f'{i} sumado correctamente')
            except ValueError as ex:
                  print(f'Elemento invalido: {i}')
      print(f'Total de la suma: {count}')
my_list1 = ['10', 'manzana', '5.5', '3', 'n/a']
sumar_valores(my_list1)
                  











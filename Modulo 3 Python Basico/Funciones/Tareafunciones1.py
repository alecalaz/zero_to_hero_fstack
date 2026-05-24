#dos funciones que impriman un mensaje diferente cada una, funcion1 llama a funcion2 y funcion2 llama a funcion1, cada una con un mensaje diferente, luego llamar a la funcion1 para ver el resultado
def print_message_1(message = " "):
  print ("Mensaje 1", message)


def print_message_2(message = " "):
  return "Mensaje 2" + message
# Llamada a las funciones
print_message_1(print_message_2())
# no se como quitar el none
#busqueda en chatgpt y cambie print en mensaje 2 con signo de suma

###

# Output: Mensaje 1 Mensaje 2
###

#def variables():
#    first_variable = "Hello"
#    print(first_variable) #NameError: name 'first_variable' is not defined 

global_variable = "Hello"
def change_global_variable():
  global global_variable #me daba error sin el global, vi la solucion en la pagina
  global_variable = "Goodbye"


change_global_variable() #esto para ejecutar la funcion y cambiar el valor de la variable
print(global_variable) # Goodbye

#funcion que sume todos los numeros de una lista
def sum_list(numbers_list):
  total = 0
  for num in numbers_list:
    total += num
  return total
# o guardar en variable
my_list = [1, 2, 3, 4, 5]
print(sum_list(my_list)) # 15

#o guardar resultado
result = sum_list(my_list)
print(result) # 15

#funcion que le de vuelta a un string
def string_reverse(string):
  return string[::-1] #busqueda de google -> metodo slicing
print(string_reverse("Hello world")) # olleH

#funcion que cuente mayusculas y minusculas en un string

def upper_lower(string):
  upper_total = 0
  lower_total = 0
  for letter in string:
    if letter.isupper():
      upper_total += 1
    elif letter.islower():
      lower_total += 1
  return f"There are {upper_total} upper cases and {lower_total} lower cases"
print(upper_lower("I love Nación Sushi")) # There are 3 upper cases and 13 lower cases


#función que acepte un string con palabras separadas por un guion y retorne un string igual pero ordenado alfabéticamente.
def order_string(string):
  words = string.split("-") #separo el string en una lista de palabras usando el guion como separador
  print(words) #para entender mejor el proceso y el orden 
  words.sort() #ordeno la lista de palabras alfabéticamente
  words_ordered = "-".join(words) #google para unir strings con "-"
  return words_ordered 
print(order_string("python-variable-funcion-computadora-monitor")) # python-variable-funcion-computadora-monitor


#Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
def is_prime(num):
    if num <= 1:
        return False
    elif num == 2 or num == 3:
        return True
    elif num % 2 == 0:
        return False
    else:
        for i in range(3, int(num**0.5) + 1, 2):  #codigo de esta linea para arriba lo hice yo, busque la formula de la raiz cuadrada de un numero para saber si es primo o no
            if num % i == 0:
                return False
        return True


def prime_list(list):
  primes = []
  for num in list:
    if is_prime(num):
      primes.append(num)
  return primes

print(prime_list([1, 4, 6, 7, 13, 9, 67])) 





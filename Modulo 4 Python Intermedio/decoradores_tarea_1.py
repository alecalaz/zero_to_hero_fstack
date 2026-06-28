# Cree un decorador que haga print de los parámetros y retorno de la función que decore.
def my_decorator(func):
    def wrapper(*args):
        print (*args)
        my_func = func(*args)
        print(my_func)
        return my_func
    return wrapper

@my_decorator
def suma(a, b):
    return a + b

suma(3, 5)

# Cree un decorador que se encargue de revisar si todos los parámetros de la función que decore son números, y arroje una excepción de no ser así.
def int_decorator(func):
    def wrapper(*args):
        for num in args:
            if not isinstance(num, (int, float)):
                raise ValueError(f'{num} no es un numero!')
        return func(*args)
    return wrapper

@int_decorator
def multiplicar(a, b):
    return a * b

multiplicar(3, 5)       # debería retornar 15
# multiplicar(3, "hola")  # debería lanzar ValueError

# Cree una clase de User que:
# Tenga un atributo de date_of_birth.
# Tenga un property de age.
# Luego cree un decorador para funciones que acepten un User como parámetro que se encargue de revisar si el User es mayor de edad y arroje una excepción de no ser así.
from datetime import date
class User():
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth
        
    
    @property
    def age(self):
        age =  date.today().year - self.date_of_birth
        return age

def age_checker(func):
    def wrapper(user, *args):
        
        if user.age > 18:
            print('Mayor de edad')
        else:
            raise ValueError('menor de edad')
        return func(user, *args)
    return wrapper

user1= User(1999)
@age_checker
def saludar(user):
    print(f"Hola, tienes {user.age} años")

saludar(user1)

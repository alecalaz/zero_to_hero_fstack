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

multiplicar(3, 5)       
# multiplicar(3, "hola")  

# Cree una clase de User que:
# Tenga un atributo de date_of_birth.
# Tenga un property de age.
# Luego cree un decorador para funciones que acepten un User como parámetro que se encargue de revisar si el User es mayor de edad y arroje una excepción de no ser así.
from datetime import date


class User:
    def __init__(self, date_of_birth):

        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = date.today()

        has_had_birthday = (
            today.month,
            today.day
        ) >= (
            self.date_of_birth.month,
            self.date_of_birth.day
        )

        return today.year - self.date_of_birth.year - (not has_had_birthday)#busque en google como hacer esta solucion


def age_checker(func):
    def wrapper(user, *args, **kwargs):
        if user.age < 18:
            raise ValueError("Menor de edad")

        print("Mayor de edad")
        return func(user, *args, **kwargs)

    return wrapper


@age_checker
def saludar(user):
    print(f"Hola, tienes {user.age} años")


user1 = User(date(1999, 8, 16))
saludar(user1)
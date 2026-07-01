#sintaxis de decorador
def decorator_name(func):
    def wrapper(parameters):
        # Logica extra
        func(parameters) # Llamada a la funcion decorada
				# Logica extra

    return wrapper

#funcion sin decorador, existen varios try o raise value error si el usuario no es 'Admin'
class User:
    role: str

    def __init__(self, role):
        self.role = role


def create_product(user, product_name):
    if user.role != "Admin":
        raise ValueError(
            "You are not allowed to run this function. You are not an admin"
        )

    # (lógica para crear producto...)
    print(f"Product {product_name} created!")


def create_product_category(user, product_category_name):
    if user.role != "Admin":
        raise ValueError(
            "You are not allowed to run this function. You are not an admin"
        )

    # (lógica para crear categoria...)
    print(f"Product Category {product_category_name} created!")


def modify_order(user, order_id):
    if user.role != "Admin":
        raise ValueError(
            "You are not allowed to run this function. You are not an admin"
        )

    # (lógica para modificar pedido...)
    print(f"Order {order_id} modified!")

#funcion con decorador para evitar DRY(dont repeat yourself)
#cuando se llama 'func()' hace referencia a la funcion que lleva el decorador.
class User:
    role: str

    def __init__(self, role):
        self.role = role


def admin_only(func):
    def wrapper(user, *args):
        if user.role != "Admin":
            raise ValueError(
                "You are not allowed to run this function. You are not an admin"
            )
        func(user, args)

    return wrapper


@admin_only
def create_product(user, product_name):
    # (lógica para crear producto...)
    print(f"Product {product_name} created!")


@admin_only
def create_product_category(user, product_category_name):
    # (lógica para crear categoria...)
    print(f"Product Category {product_category_name} created!")


@admin_only
def modify_order(user, order_id):
    # (lógica para modificar pedido...)
    print(f"Order {order_id} modified!")


###Decorador 'property'
class Student:
    spanish_score: int
    english_score: int

    def __init__(self, spanish_score, english_score):
        self.spanish_score = spanish_score
        self.english_score = english_score

    @property
    def average_score(self):
        return (self.spanish_score + self.english_score) / 2


student_ian = Student(80, 80)
print(f"Average score: {student_ian.average_score}")

student_ian.spanish_score = 50
print(f"Average score: {student_ian.average_score}")

from datetime import date


class User:
    date_of_birth: date

    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        # Debemos calcular la edad cada vez que la usemos
        # ya que va a variar dependiendo de la fecha actual
        today = date.today()
        return (
            today.year
            - self.date_of_birth.year
            - (
                (today.month, today.day)
                < (self.date_of_birth.month, self.date_of_birth.day)
            )
        )


my_user = User(date(1990, 1, 1))
print(f"Age: {my_user.age}")

#Decorador Class Method
#no se necesita instanciar la clases, es decir, no es encario crear el objeto y luego llamar el metodo. Se puede llamar el metodo de una vez y va a a crear el objeto automaticamente

from datetime import datetime


class Person:
	def __init__(self, first_name, last_name):
            self.first_name = first_name
            self.last_name = last_name


class User:
    def __init__(self, email, password, person):
        self.email = email
        self.password = password
        self.person = person

    @classmethod
    def create_user(cls, first_name, last_name, email, password):
        person = Person(first_name, last_name)
        return User(email, password, person)


my_user = User.create_user("Sarah", "Connor", "sconor@gmail.com", "321")
print("User: ", vars(my_user))
print("Person: ", vars(my_user.person))


from datetime import datetime


users = [
    {"email": "a@gmail.com", "password": "123"},
]


class User:
    email: str
    password: str

    def __init__(self, email, password):
        self.email = email
        self.password = password

    @classmethod
    def try_login(cls, email, password):
        for user in users:
            if user["email"] == email and user["password"] == password:
                print("Login successful")
                return User(email, password)

        raise ValueError("Wrong credentials")

    @classmethod
    def register(cls, email, password):
        users.append({"email": email, "password": password})
        return User(email, password)


my_new_user = User.register("c@gmail.com", "123")
User.try_login("c@gmail.com", "123")
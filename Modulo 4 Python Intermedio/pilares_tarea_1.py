# Cree una clase de BankAccount que:
# Tenga un atributo de balance.
# Tenga un método para ingresar dinero.
# Tengo un método para retirar dinero.
# Cree otra clase que herede de esta llamada SavingsAccount que:
# Tenga un atributo de min_balance que se pueda asignar al crearla.
# Arroje un error si al intentar retirar dinero, el retiro haría que el balance quede debajo del min_balance. Es decir que sí se pueden hacer retiros siempre y cuando el balance quede arriba del min_balance.
# Cree una clase abstracta de Shape que:
# Tenga los métodos abstractos de calculate_perimeter y calculate_area.
# Ahora cree las siguientes clases que hereden de Shape e implementen esos métodos: Circle, Square y Rectangle.
# Cada una de estas necesita los atributos respectivos para poder calcular el área y el perímetro.
# Investigue qué usos se le pueden dar a la herencia multiple y cree un ejemplo
from abc import abstractmethod, ABC
from math import pi
class BankAccount():
    def __init__(self, balance):
        self.balance = balance
        
        
    
    def deposit(self, amount):
        self.balance += amount
    

    def withdraw(self, amount):
        if amount > self.balance:
            print('insufficient funds!')
        else:
            self.balance -= amount
            

class SavingsAccount(BankAccount):
    def __init__(self,balance, min_balance):
        super().__init__(balance)
        self.min_balance = min_balance
        
        
    

    def withdraw(self, amount):
        if self.balance - amount <  self.min_balance:
            raise ValueError
        else:
            self.balance -= amount

    
class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return pi * (self.radius ** 2)
    
    def calculate_perimeter(self):
        return 2 * pi * self.radius


class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def calculate_area(self):
        return self.side ** 2
    
    def calculate_perimeter(self):
        return 4 * self.side


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width * self.height
    
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)
    

        
#ejemplo de herencia multiple, se me ocurre un atleta que haga natacion y atletismo
class Swimmer:
    def swim(self):
        return "I can swim"

class Runner:
    def run(self):
        return "I can run"

class Triathlete(Swimmer, Runner):
    def __init__(self, name):
        self.name = name

    def compete(self):
        return f"{self.name}: {self.swim()} {self.run()}"

#Herencia. Clases pueden heredar atributos y metodos  de otras clases
class Vehicle:
    is_on = False
    wheel_number = 0

    def turn_on(self):
        self.is_on = True
        print(f"Vehicle with {self.wheel_number} wheels is on")

    def turn_off(self):
        self.is_on = False
        print(f"Vehicle with {self.wheel_number} wheels is off")

class Car(Vehicle):
    wheel_number = 4


my_car = Car()
my_car.turn_on()
my_car.turn_off()

class Bike(Vehicle):
    wheel_number = 2


my_bike = Bike()
my_bike.turn_on()
my_bike.turn_off()

#Herencia Multiple
class WalkerMixin:
  def walk(self):
    print("I'm walking!")

class RunnerMixin:
  def run(self):
    print("I'm running!")

class FlyerMixin:
  def fly(self):
    print("I'm flying!")

class SuperMan(WalkerMixin, RunnerMixin, FlyerMixin):
  pass

clark_kent = SuperMan()
clark_kent.walk()
clark_kent.run()
clark_kent.fly()

#Si hay herencia multiples, y hay atributos y metodos que se llamen igual, el que tiene precedencia es el que esta de primero.

#Clases abstractas. No se pueden instanciar.( o sea no se pueden crear objetos pero se utiliza para que otras clases hereden atributos y metodos de la clase padre abstracta)

#Metodos abstractos, deben ser sobre escritos por sus clases hijas

#metodos abstractos, se utiliza cuando usted tiene que utilizar el metodo, pero desarrollarlo a su manera

from abc import ABC, abstractmethod


class Animal(ABC):
	def breath(self):
		pass

	def born(self):
		pass

	@abstractmethod
	def reproduce(self):
		# Todas las especies de animales deben reproducirse para sobrevivir
		# Pero lo pueden hacer de distintas maneras
		pass

class AsexualAnimal(Animal):
	def reproduce(self):
		print("Reproducing in an asexual manner")

class SexualAnimal(Animal):
	def reproduce(self, mate):
		print(f"Reproducing in a sexual manner with {mate}")

class OtherAnimal(Animal):
	pass


asexual_animal = AsexualAnimal()
asexual_animal.reproduce() # -> Reproducing in an asexual manner 

sexual_animal_a = SexualAnimal()
sexual_animal_b = SexualAnimal()
sexual_animal_b.reproduce(sexual_animal_b) # -> Reproducing in a sexual manner with sexual_animal_b

animal = Animal() # va a fallar porque Animal es una clase abstracta
other_animal = OtherAnimal() # va a fallar porque no se sobre-escribió el método reproduce

from abc import ABC, abstractmethod
#ABC indica que la clases es abstracta
class ReportEmailer(ABC):
	@abstractmethod
	def generate_report():
		# genera el reporte
		pass

	def email_report():
		# envia el report por email
		pass

	def generate_report_and_email(self):
		self.generate_report()
		self.email_report()
		

###Encapsulamiento 

# public: pueden ser accesados desde cualquier lugar.
# protected: pueden ser accesados desde los métodos de la clase y sus clases hijas.
# private: pueden ser accesados solo desde los métodos de la clase.
# name es publico.
# _name es protected.
# __name es privado.
# get_age es publico.
# _get_age es protected.
# __get_age es privado.
#Python carece de esta funcionalidad, pero si hipotéticamente, funcionaría así:
class Person:
	pass
    # name: string #public
	# date_of_birth: datetime #protected
	# __sex: string # private

	# def __init__(self, name, date_of_birth, sex)
	# 	self.name = name
	# 	self._date_of_birth = date_of_birth
	# 	self.__sex = sex

class Worker(Person):
	def print_date_of_birth(self):
		print(self._date_of_birth)

	def print_sex(self):
		print(self.__sex)

my_person = Person("Juan", "2003/02/02", "Male")
print(my_person.name) # -> Juan
print(my_person._date_of_birth) # -> error, ya que _date_of_birth es un atributo protegido
print(my_person.__sex) # -> error, ya que __sex es un atributo privado

my_worker = Worker("Joan", "1984/05/06", "Female")
my_worker.print_date_of_birth() # -> 1984/05/06
my_worker.print_sex() # -> error, ya que __sex es un atributo privado

#Abstraccion

#Polimorfismo
# Viene de poli (varias) morfo (formas).
# Se refiere a que una sintaxis o método con el mismo identificador pueden tener comportamientos o formas distintas dependiendo del contexto en que se usen.
# Por ejemplo, la función range dependiendo del numero de parámetros que tenga.
# Otro ejemplo es el símbolo de +.
# En el caso de los objetos, podemos estandarizar ciertos identificadores para poder usarlos de manera intercambiable con clases que no estén relacionadas.
# Por ejemplo, el método reproduce del ejemplo de arriba es un caso de polimorfismo.
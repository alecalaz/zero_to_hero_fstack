#veo las clases como fabricas de objetos, carros, articulos, etc
#los atributos son las "cualidades del los objetos"
#class car:
    #wheels =4
    #electric_windows = True

class variables:
    pass

my_new_variable = variables()
my_new_variable.new_value = 0
print(my_new_variable.new_value)


class Car:
	wheel_number = 4
	
	def my_first_method(self):
		print("Hello OOP World!")

	def show_history(self, miles, crashes):
		print(f"This car has {miles} miles and {crashes} crashes")
		
		
my_car = Car()
my_car.show_history(45000, 2)

#self es para guardar el valor del objeto
class Car:
	wheel_number = 4
	
	def my_first_method(self):
		print("Hello OOP World!")

	def show_history(self, miles, crashes):
		print(f"This car has {miles} miles, {crashes} crashes and {self.wheel_number} wheels")
		
		
my_car = Car()

my_truck = Car()
my_truck.wheel_number = 6

my_bigger_truck = Car()
my_bigger_truck.wheel_number = 8


my_car.show_history(45000, 2)
my_truck.show_history(45000, 2)
my_bigger_truck.show_history(45000, 2)


#constructores con atributos
class Person():
	def __init__(self, name):
		print(f"Ha nacido una persona llamada {name}!")
		self.name = name
		self.age = 0

person_1 = Person("John")
print(person_1.age)
print(person_1.name)

# name no es lo mismo que self.name
# age no es lo mismo que person_1.age
# variable no es lo mismo que self.variable

class Car:
    def __init__(self, brand, line, model, color):
        self.brand = brand
        self.line = line
        self.model = model
        self.color = color


my_audi = Car("Audi", "A4", 2023, "Red")
my_bmw = Car("BMW", "X5", 2021, "Green")
my_ferrari = Car("Ferrari", "Enzo", 1999, "Red")

#mas ejemplos
class PhotographyCamera:
	photographies = []

	def __init__(self, storage_size_in_mb):
		# each photo takes around 10mb
		self.max_photographies = storage_size_in_mb / 10
	
	def take_photo(self, photography):
		if len(self.photographies) >= self.max_photographies:
			print("My storage is full!")
			return

		self.photographies.append(photography)
		
kodak_camera = PhotographyCamera(50)
kodak_camera.take_photo("My car")
kodak_camera.take_photo("My house")
print(kodak_camera.photographies)


#Person
class Person():
	def __init__(self, name):
		self.name = name
		self.age = 0
		age = 56

person_1 = Person("John")
age = 34

print(person_1.age)
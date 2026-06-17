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
# Cree una clase Rectangle que:
# Tenga atributos width y height
# Tenga un método get_area() que retorne el área
# Tenga un método get_perimeter() que retorne el perímetro
# Valide que ningún valor sea negativo. Si lo es, lance una excepción con un mensaje adecuado

class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height= height
        if self.width < 0 or self.height < 0:
            raise ValueError("Existe un valor negativo, los valores deben ser positivos")

    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * (self.width + self.height)
    

# Cree una clase base Animal y dos clases hijas Dog y Cat:
# Animal debe tener nombre y método speak() que retorne "Hace un sonido"
# Dog debe sobrescribir speak() para decir "Guau"
# Cat debe sobrescribir speak() para decir "Miau"

class Animal():

    def __init__(self, name):
        self.name = name

    
    def speak(self):
        return 'Hace un sonido'

class Dog(Animal):

    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return 'Guau'
    
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def speak(self):
        return 'Miau'


# Cree una clase Product con:
# Nombre, precio y cantidad
# Cree una clase Inventory que:
# Guarde productos en una lista
# Tenga métodos para:
# Agregar un producto
# Mostrar todos los productos
# Calcular el valor total del inventario
    
class Product():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        

class Inventory():
    
    def __init__(self):
        self.my_list = []
    
    def add_product(self, product):
        self.my_list.append(product)
    
    def show_product(self):
        for product in self.my_list:
            print (f'{product.name}, {product.price}, {product.quantity}')
    
    def total_value(self):
        total = 0
        for product in self.my_list:
            total += product.price * product.quantity
        return total

        


    
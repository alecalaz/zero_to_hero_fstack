#clase Person
class Person():
    def __init__(self, name):
        self.name = name
        self.age = 0
        age = 56

person_1 = Person("John")
person_2 = Person("Luis")
person_3 = Person("Ale")

#clase circle, calcula el area
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        area = (self.radius ** 2) * 3.14
        return area

circle1 = Circle(6)
circle1_area = circle1.get_area()
print(circle1_area)

#ejercicio de bus
class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []
        

    def add_passenger(self, passenger):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(passenger)
        elif len(self.passengers) == self.max_passengers:
            print('El bus esta lleno')
    def remove_passenger(self,):
        if len(self.passengers) > 0:
            self.passengers.pop()
        else:
            print('El bus ya esta vacio')

    

bus1 = Bus(10)
bus1.add_passenger(person_1)
bus1.add_passenger(person_2)
bus1.add_passenger(person_3)
bus1.remove_passenger()
bus1.remove_passenger()
bus1.remove_passenger()
bus1.remove_passenger() #genera mensaje de que el bus ya esta vacio

class Head:
    def __init__(self):
        pass

class Arm:
    def __init__(self, hand):
        self.hand = hand

class Hand:
    def __init__(self):
        pass

class Leg:
    def __init__(self, feet):
        self.feet = feet
    
class Feet:
    def __init__(self):
        pass

class Torso:
    def __init__(self, head, right_arm, left_arm, right_leg, left_leg):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg

class Human:
    def __init__(self, torso):
        self.torso = torso
        pass


head = Head()
left_feet = Feet()
left_hand = Hand()
right_feet = Feet()
right_hand = Hand()
left_arm = Arm(left_hand)
right_arm = Arm(right_hand)
left_leg = Leg(left_feet)
right_leg = Leg(right_feet)
torso = Torso(head, right_arm, left_arm, right_leg, left_leg)
human = Human(torso)










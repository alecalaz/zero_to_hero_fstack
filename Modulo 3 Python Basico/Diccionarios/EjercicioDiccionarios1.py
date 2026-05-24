#generar diccionario de un hotel
my_hotel = {
    "name": "Double tree by hilton",
    "number_of_stars": 4,
    "rooms": [
        {"number":100, "floor":1, "price_per_night": 100},
        {"number":101, "floor":1, "price_per_night": 100},
        {"number":102, "floor":1, "price_per_night": 100},
        {"number":103, "floor":1, "price_per_night": 100},
        {"number":104, "floor":1, "price_per_night": 100},
        {"number": 200, "floor": 2, "price_per_night": 150},
        {"number": 201, "floor": 2, "price_per_night": 150},
        {"number": 300, "floor": 3, "price_per_night": 200},
        {"number": 301, "floor": 3, "price_per_night": 200}
    ]
}

#diccionario usando dos listas de mismo tamaño
list_a = ["first_name", "last_name", "role"]
list_b = ["Alejandro", "Calderon", "Cloud Engineer"]
counter = 0

employee_info = {}
while counter < len(list_a):
    for i in range(len(list_a)):
        employee_info[list_a[i]] = list_b[i]
    counter += 1
print(employee_info)

#lista para eliminar keys en un diccionario
employee = {"name": "Alejandro", "age": 27, "email": "alejandro@lyfter.com", "access_level": 5}
list_keys_to_remove = ["email", "access_level", "age"]
for key in list_keys_to_remove:
    employee.pop(key)
print(employee)
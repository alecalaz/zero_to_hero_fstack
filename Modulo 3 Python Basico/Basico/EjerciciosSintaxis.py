#1. Ejercicio de clasificación por edad
name = input("Por favor ingresa tu nombre: ")
last_name = input("Por favor ingresa tu apellido: ")
age = int(input("Por favor ingresa tu edad: "))

if age < 2:
    print(f"Hola {name} {last_name}, eres un bebé")
elif age < 7:
    print(f"Hola {name} {last_name}, eres un niño")
elif age < 13:
    print(f"Hola {name} {last_name}, eres un preadolescente")
elif age < 18:
    print(f"Hola {name} {last_name}, eres un adolescente")
elif age < 30:
    print(f"Hola {name} {last_name}, eres un joven adulto")
elif age < 60:
    print(f"Hola {name} {last_name}, eres un adulto")
else:
    print(f"Hola {name} {last_name}, eres un adulto mayor")

#2. crear numuero secreto y pedir que adivine
from random import randint
secret_number = randint(1, 10)
guess = int(input("Adivina el número secreto entre 1 y 10: "))
while not guess == secret_number:
    print(f"Lo siento, el número secreto era {secret_number}, intenta de nuevo")
    guess = int(input("Adivina el número secreto entre 1 y 10: "))
else:
    print(f"¡Felicidades! Has adivinado el número secreto {secret_number}")

#3. 3 numeros y muestre el mayor
print("Vas a ingresar 3 números y te diré cuál es el mayor")
num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))
num3 = int(input("Ingresa el tercer numero: "))
if num1 >= num2 and num1 >= num3:
    print(f"El número mayor es: {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"El número mayor es: {num2}")
else:
    print(f"El número mayor es: {num3}")

#4. Promedio de notas de un usuario, cantidad de notas aprobadas y reprobadas, promedio de cada una
num_notes = int(input("¿Cuántas notas quieres ingresar? "))
counter = 0
total = 0
total_approved = 0
total_not_approved = 0
notes_approved = 0
notes_not_approved = 0
average_approved = 0    
average_not_approved = 0   

while counter < num_notes:
    note = int(input(f"Ingresa la nota {counter + 1}: "))
    total += note
    counter += 1

    if note >= 70:
        notes_approved += 1
        total_approved += note
        average_approved = total_approved / notes_approved
    else:
        notes_not_approved += 1
        total_not_approved += note
        average_not_approved = total_not_approved / notes_not_approved

average_total = total / num_notes
print(f"El promedio total de las notas es: {average_total}")
print(f"El promedio de las notas aprobadas es: {average_approved}")
print(f"El promedio de las notas reprobadas es: {average_not_approved}")

#5. Pedir precio producto y calcular descuento
price = float(input("Ingresa el precio del producto: "))
if price < 100:
    discount = price * 0.02
    price_with_discount = price - discount
    print(f"El precio con descuento es: {price_with_discount}")
elif price >= 100:
    discount = price * 0.1
    price_with_discount = price - discount
    print(f"El precio con descuento es: {price_with_discount}")

#6. Pedir tiempo en segundos y calcular si es menor o mayor a 10 minutos
time_seconds = int(input("Ingresa el tiempo en segundos: "))
time_10min = 600
if time_seconds < time_10min:
    seconds_left = time_10min - time_seconds
    print(seconds_left)
elif time_seconds > time_10min:
    print("Mayor")
else:
    print("Igual")

#7. Pedir numero y hacer suma de 1 hasta el numero ingresado
number = int(input("Ingresa un número: "))
counter = 1
sum = 0
while counter <= number:
    sum = counter + sum
    counter += 1

print(f"La suma de 1 hasta {number} es: {sum}")

#8. Pedir 3 numeros y mostrar si contiene 30 o la suma de sus num es 30
number = int(input("Ingresa un número: "))
number2 = int(input("Ingresa segundo número: "))
number3 = int(input("Ingresa tercer número: "))
if number == 30 or number2 == 30 or number3 == 30:
    print("Correcto")
elif number + number2 + number3 == 30:
    print("Correcto")
else:
    print("Incorrecto")

#9. Convertir grados Celsius a Fahrenheit y Kelvin
celsius = int(input("Ingresa la temperatura en grados Celsius: "))
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15
print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit")
print(f"{celsius} grados Celsius son {kelvin} grados Kelvin")

#10. Ingrese un numero del 1 al 10 y muestre su tabla de multiplicar
number = int(input("Ingrsa un numero del 1 al 10: "))
if number >= 1 and number <= 10:
    print(f"Tabla de multiplicar del {number}:")
    for num in range(1, 11):
        result = number * num
        print(f"{number} x {num} = {result}")
#2. crear numuero secreto y pedir que adivine
from random import randint
secret_number = randint(1, 10+1)
guess = int(input("Adivina el número secreto entre 1 y 10: "))
while not guess == secret_number:
    print(f"Lo siento, el número secreto era {secret_number}, intenta de nuevo")
    guess = int(input("Adivina el número secreto entre 1 y 10: "))
else:
    print(f"¡Felicidades! Has adivinado el número secreto {secret_number}")

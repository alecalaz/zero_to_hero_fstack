print("---- Clasificador de Nivel Gamer ----")
name = input("Ingresa tu nombre: ")
hours = int(input("¿Cuántas horas juegas a la semana? "))
is_competitive = input("juegas competitivo? (sí/no): ").lower()
if hours < 10:
    category = "Novato"
    message = (f"Bienvenido {name} al mundo gamer")
elif hours < 50:
    category = "Casual"
    message = (f"Ya le estas agarrando el ritmo {name}")
elif hours < 200:
    category = "Gamer"
    message = (f"Definitivamente sabes lo que haces {name}")
elif hours >= 200 and is_competitive == "sí":
    category = "Pro Gamer"
    message = (f"Eres una leyenda {name}!")
else:
    category = "Gamer"
    message = ("Tienes la experiencia, pero aun no entras al competitivo")
print(f"{name}, tu categoría gamer es: {category}")
print(message)
# Pseudocódigo para calcular descuento

price = int(input("Ingrese el precio del producto: "))
if price < 100:
    discount = price * 0.02
    final_price = int(price - discount)
else:
    discount = price * 0.1
    final_price = int(price - discount)

print(f"El precio final del producto es: {final_price}")


#Cree un pseudocódigo que le pida un `tiempo en segundos` y calcule si es mayor o menor a 10minutos
time_in_seconds = int(input("Ingrese el tiempo en segundos: "))
if time_in_seconds < 600:
    seconds_left = 600 - int(time_in_seconds)
    print("El tiempo es menor a 10 minutos")
    print(f"Quedan {seconds_left} segundos para llegar a 10 minutos")
elif time_in_seconds > 600:
    print("Mayor a 10 minutos")
else:
    print("El tiempo es exactamente 10 minutos")



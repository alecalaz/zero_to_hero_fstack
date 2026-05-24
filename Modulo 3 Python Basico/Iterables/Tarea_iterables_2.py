#contar cuantas veces aparece un elemento en una lista
my_list = input("Ingrese una lista de numeros separados por comas: ").split(",")
num_to_count = input("Ingrese el numero que desea contar: ")
count = 0
for num in my_list:
    num = num.strip()
    if num == num_to_count:
        count += 1
print(f" El numero {num_to_count} aparece {count} veces en la lista.")


#verificar si todos los elementos de una lista son positivos
my_list_1 = [1, 2, 3, 4, 5]
all_positive = True
for num in my_list_1:
    if num < 0:
        print("Hay al menos un número negativo o cero")
        all_positive = False

if all_positive:
    print("Todos los numeros son positivos")


#encontrar el menor numero de una lista sin usar min()
my_list = [9, 4, 7, 1, 5]
min_num = my_list[0]
for num in my_list:
    if num < min_num:
        min_num = num
print(f"El numero menor de la lista es: {min_num}")

#Cree un programa que reciba una lista de números y calcule el promedio de los valores, luego cree una nueva lista con solo los valores mayores al promedio

my_list = [10, 20, 30, 40, 50]

total = 0
average = 0
for num in my_list:
    total = total + num
average = total / len(my_list)

list_bigger_than_average = []
for num in my_list:
    if num > average:
        list_bigger_than_average.append(num)
print(f"""
      Promedio : {average}
      Nueva lista: {list_bigger_than_average}
""")


#Cree un programa que le pida al usuario ingresar 5 palabras. Luego muestre una nueva lista con solo aquellas palabras que tengan más de 4 letras
words = input("Ingrese 5 palabras separadas por comas: ").split(",")
words_longer_than_4 = []
for word in words:
    if len(word) > 4:
        words_longer_than_4.append(word)

if len(words_longer_than_4) == 0:
    print("No hay palabras con mas de 4 letras")
else:
    print(words_longer_than_4)



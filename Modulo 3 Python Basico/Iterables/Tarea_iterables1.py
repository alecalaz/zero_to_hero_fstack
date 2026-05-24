#1 iterar por listas e imprimir cada elemento al mismo tiempo
#dificultad media
first_list = ['Hay', 'en', 'que', 'iteracion', 'indices', 'muy']
second_list = ['casos', 'los', 'la', 'por', 'es', 'util']
for i in range(len(first_list)):
    print(first_list[i], second_list[i])

#2 string letra por letra de derecha a izquierda
#range se define inicio, fin y salto entre numeros
#primero es inclusivo, segundo exlusivo, tercero es el salto entre numeros,-1 para ir de derecha a izquierda
#dificulta media, buscar en google funciones range
string = "Pizza con jamon"
for index in range(len(string)-1, -1, -1):
    print(string[index])

#3 intercambiar primer y ultimo elemento de una lista
#dificultad facil
my_list = [4, 3, 6, 1, 7]
first = my_list[0]
last = my_list[-1]
my_list[0] = last
my_list[-1] = first
print(my_list)

#4 crear programa que elimine numeros impares de una lista
#dificultad facil
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = []
for number in (numbers_list):
    if number % 2 == 0:
        even_list.append(number)
print(even_list)


#5 pedir al usuario 10 numeros, mostrar todos los numeros y mostrar el mas alto

numbers = []
counter = 0
while counter < 10:
    number = int(input(f"Ingresa 10 numeros: "))
    numbers.append(number)
    counter = counter + 1
#buscar como sacar el numero mas alto de una lista en google
print(f"Los numeros ingresados son: {numbers}. El mas alto es: {max(numbers)}")

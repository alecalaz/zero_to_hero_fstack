
#Sumas entre diferentes tipos de datos
#1. Suma de un numero entero y un numero decimal
num1 = 5
num2 = 3.5
result = num1 + num2
print(f"La suma de {num1} y {num2} es: {result}")

string1 = "hola"
string2 = "mundo"
string3 = string1 + string2
print(string3)

#se arregla agregando "str" antes de num1
print(string3 + str(num1))

#se arregla de la misma manera agregando "str" antes de list1
list1 = [1, 2, 3]
print(string3 + str(list1))

#Da 1?
print(True + False)
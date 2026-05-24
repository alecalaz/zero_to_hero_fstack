
para hacer cambios en una lista, se necesita usar un for loop en un range de la lista
my_list = [ 1, 2, 3, 4, 5, 6]
for index in range(len(mylist))

usar while cuando no hay certeza de cuanto va a durar la funcion

---Funcion enumerate----

for index, item in enumerate(my_list):
	print (f"item es {index} con {item})

==break== para romper el ciclo de una lista

==continue== para brincarse un elemento en una list


## ==Listas deep==

Agregar datos = .append

my_list = [2, 3, 4]
my_list.append(5)

print(my_list)

output
2 3 4 5

Insertar datos = .insert
my_list = [2, 3, 4]
my_list.inser(1, 6) #1 es el numero de indice y 6 el valor que quiero insertar

output
2 6 3 4

Extender listas = .extend

my_list = [1, 2, 3]
my_list_2 = [4,5,6]

my_list.extend(my_list_2)

output
1,2,3,4,5,6

eliminar un elemento = .pop

my_list = [1, 2, 3, 4]
my_list.pop(0)

outpout
2 3 4




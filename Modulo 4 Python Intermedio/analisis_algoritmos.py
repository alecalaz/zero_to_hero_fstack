#como analizar algortimos
#se pueden analizar por su uso de memoria(cuantas unidades necesito o procesamiento) o su uso tiempo de ejecucion(cuantos pasos para llegar al objetivo)
#variande cual sea del input del algoritmo
#la manera mas comun es por el tiempo de ejecucion para analizar

####
#Big O Notation
####

#representa el rendimiento del algoritmo en el pero de los casos
#utiliza funcionas algebraicas

#las mas utilizadas son O(n2), O(log n) y O(n)

#O1 ejemplo
# Todas las instrucciones del código son de tiempo constante, u O(1), siempre y cuando:
# No sean ciclos ni recursividad.
# No sean llamadas a funciones que no son de tiempo constante (que contienen ciclos o recursividad).

def get_max_number(number1, number2):
	if number1 > number2: # O(1)
		return number1 # O(1)
			
	return number2 # O(1)


my_number_1 = 56 # O(1)
my_number_2 = 75 # O(1)

max_number = get_max_number(my_number_1, my_number_2) # O(1) porque la función es O(1)
print(max_number) # O(1)

#ejemplo de O(n)

# for x in range(n): # O(n)
	

#ejemplo O(n2)
	# for i in range(n): # O(n)
	#   for j in range(n): # O(n^2)
	# 	    for k in range(n): # O(n^3)
	# 		    for l in range(n): # O(n^4)
	

#ejemplo O(log n)
#el tiempo dismunye en cuanto mas grande sea el input
# for i in range(0, n, n / i): # O(log n)

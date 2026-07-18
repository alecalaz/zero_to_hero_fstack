def bubble_sort(list_to_sort):
    for outer_index in range(0, len(list_to_sort)-1):#O(n)
        has_made_changes = False#O(1)
        for index in range(0, len(list_to_sort)-1 - outer_index):#O(n2)
            current_element = list_to_sort[index]#O(1)
            next_element = list_to_sort[index + 1]#O(1)
            if current_element > next_element:#O(1)
                list_to_sort[index] = next_element#O(1)
                list_to_sort[index + 1] = current_element#O(1)
                has_made_changes = True#O(1)
        if not has_made_changes:#O(1)
            return#O(1)
        

def print_numbers_times_2(numbers_list):
	for number in numbers_list:#O(n)
		print(number * 2)#O(1)

def check_if_lists_have_an_equal(list_a, list_b):
	for element_a in list_a:#O(n)
		for element_b in list_b:#O(n2)
			if element_a == element_b:#O(1)
				return True#O(1)
				
	return False#O(1)

def print_10_or_less_elements(list_to_print):
	list_len = len(list_to_print)#O(1)
	for index in range(min(list_len, 10)):#O(1) #nunca imprime mas de 10 elementos. tamaño fixed por eso O1
		print(list_to_print[index])#O(1)
		
def generate_list_trios(list_a, list_b, list_c):
	result_list = []#O(1)
	for element_a in list_a:#O(n)
		for element_b in list_b:#O(n2)
			for element_c in list_c:#O(n3)
				result_list.append(f'{element_a} {element_b} {element_c}')#O(1)
				
	return result_list #O(1)
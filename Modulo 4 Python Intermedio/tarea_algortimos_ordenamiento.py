def bubble_sort(list_to_sort):
    for outer_index in range(0, len(list_to_sort)-1):
        has_made_changes = False
        for index in range(0, len(list_to_sort)-1 - outer_index):
            current_element = list_to_sort[index]
            next_element = list_to_sort[index + 1]
            if current_element > next_element:
                list_to_sort[index] = next_element
                list_to_sort[index + 1] = current_element
                has_made_changes = True
        if not has_made_changes:
            return



def reverse_bubble_sort(list_to_sort):
    for outer_index in range(0, len(list_to_sort) - 1):
        has_made_changes = False
        for index in range( len(list_to_sort) -1, outer_index, -1 ):#un range funciona (inicio, fin, paso)
            #queremos que el fin sea el outer_index por que una vez el menor este ordenado no queremos visitar nuevamente y compararlo
            current_element = list_to_sort[index]
            previous_element = list_to_sort[index - 1]
            if current_element < previous_element:
                list_to_sort[index] = previous_element
                list_to_sort[index -1] = current_element
                has_made_changes = True
            #agregar el range
            #comparar indices de derecha a izquierda
            #avanzar en negativo ([-1])
            #Si es menor, cambiar hasta que el mas peque;o quede en el primer indice e ignorar en las siguientes pasadas
        if not has_made_changes:
            return
my_test_list = [18, -11, 68, 6, 32, 53, -23]
test_list_2 = [18, -11, 68, 6, 32, 53, -23]
reverse_bubble_sort(my_test_list)
bubble_sort(test_list_2)
print(my_test_list)
print(test_list_2)


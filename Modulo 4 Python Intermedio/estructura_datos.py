class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    head: Node

    def __init__(self, head):
        self.head = head

    def print_structure(self):
        current_node = self.head
        print(current_node.data)

        current_node = current_node.next
        print(current_node.data)

        current_node = current_node.next
        print(current_node.data)


third_node = Node("Soy el tercer nodo")
second_node = Node("Soy el segundo nodo", third_node)
first_node = Node("Soy el primer nodo", second_node)

linked_list = LinkedList(first_node)
linked_list.print_structure()


#enciclando el .next
class Node:
	data: str
	next: "Node"

	def __init__(self, data, next=None):
		self.data = data
		self.next = next

class LinkedList:
	head: Node

	def __init__(self, head):
		self.head = head

	def print_structure(self):
		current_node = self.head

	while (current_node is not None):
		print(current_node.data)
		current_node = current_node.next


third_node = Node("Soy el tercer nodo")
second_node = Node("Soy el segundo nodo", third_node)
first_node = Node("Soy el primer nodo", second_node)

linked_list = LinkedList(first_node)
linked_list.print_structure()


#primero tenemos el objeto 'Node'
class Node:
    data : str # tiene una lista de strings como data
    next : 'Node'
    def __init__(self, data): #constructor
       self.data = data

#segundo la clase LinkedList (por que estamos trabajando linked list)
class LinkedList:
	head : Node #Tiene un atributo head
    
	def __init__(self, head):
		self.head = head
	def print_structure(self):
		current_node = self.head
		print(current_node.data)
		
first_node = Node('Hola Mundo')
structure = LinkedList(first_node)
structure.print_structure()
            
	
###QUEUE
#FIFO(First in First Out)
#Dos metodos dequeue/ enqueue

#Stack(pila)
#como una pila de platos, ultimo que entra, primero que sale
#si quiero el del medio, tengo que sacar todos
#metodos push y pop

#Double Ended Queue
#tiene 4 metodos
#push_right, push_left, pop_right, pop_left

#Binary Tree
#Se basa en los Linked List
#Tiene un nodo root

	
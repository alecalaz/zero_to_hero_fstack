class Node:
	data: str
	next: "Node"

	def __init__(self, data, next=None):
		self.data = data
		self.next = next

class Queue:
	head: Node

	def __init__(self, head):
		self.head = head

	def print_structure(self):
		current_node = self.head

		while current_node is not None:
			print(current_node.data)
			current_node = current_node.next
	
	def enqueue(self, new_node):
		current_node = self.head

		while current_node.next is not None:
			print(current_node.data)
			current_node = current_node.next
		
		print(current_node.data)
		current_node.next = new_node

		print('Nuevo ciclo')
		current_node = self.head
		while(current_node is not None):
			print(current_node.data)
			current_node = current_node.next
		
	def dequeue(self):
		if self.head:
			self.head = self.head.next


first_node = Node('Soy el primero')
second_node = Node('Soy el segundo')
first_node.next = second_node
third_node = Node('Soy el tercero')
second_node.next = third_node

structure = Queue(first_node)

fourth_node = Node('Soy el cuarto')
structure.enqueue(fourth_node)
structure.print_structure()




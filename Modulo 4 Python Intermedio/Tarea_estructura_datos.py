# Cree una estructura de objetos que asemeje un Stack.
# Debe incluir los métodos de push (para agregar nodos) y pop (para quitar nodos).
# Debe incluir un método para hacer print de toda la estructura.
# No se permite el uso de tipos de datos compuestos como lists, dicts o tuples ni módulos como collections.

class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
    

class Stack:
    def __init__(self):
        self.top = None
    
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
    
    def print_stack(self):
        current_node = self.top
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
    
    def pop(self):
        if self.top is None:
            raise ValueError('Lista vacia')
        
        self.top = self.top.next

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)


print(stack.top.next.next.data)

# Cree una estructura de objetos que asemeje un Double Ended Queue.
# Debe incluir los métodos de push_left y push_right (para agregar nodos al inicio y al final) y pop_left y pop_right (para quitar nodos al inicio y al final).
# Debe incluir un método para hacer print de toda la estructura.
# No se permite el uso de tipos de datos compuestos como lists, dicts o tuples ni módulos como collections.

#push_left cambia:
# nuevo.next

# head.previous

# head

#push_right cambia:
# nuevo.previous

# tail.next

# tail
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
    def push_left(self, data):
        new_node = Node(data)
        if self.head is None:
            
            self.head = new_node
            self.tail = new_node
        else:
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node
    def push_right(self, data):
        new_node = Node(data)
        if self.tail is None:           
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
    def pop_left(self):
        
        if self.head is None:
            raise ValueError('queue esta vacio!')
        
        deleted_node = self.head
        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.previous = None
        return deleted_node.data
    
    def pop_right(self):
        if self.tail is None:
            raise ValueError('queue esta vacio')
        deleted_node = self.tail
        if self.tail.previous is None:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.previous
            self.tail.next = None
        return deleted_node.data
    def print_stack(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

# Cree una estructura de objetos que asemeje un Binary Tree.
# Debe incluir un método para hacer print de toda la estructura.
# No se permite el uso de tipos de datos compuestos como lists, dicts o tuples ni módulos como collections
#stackoverflow
#reddit
#w3
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert_recursive(self.root, data)

    def insert_recursive(self, current_node, data):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert_recursive(current_node.left, data)
        else:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert_recursive(current_node.right, data)

    def print_tree(self):
        self._print_recursive(self.root)

    def print_recursive(self, current_node):
        if current_node is not None:
            self._print_recursive(current_node.left)
            print(current_node.data)
            self._print_recursive(current_node.right)


            




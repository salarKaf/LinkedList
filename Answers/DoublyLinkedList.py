

from LinkList import LinkedList
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def make_doubly(self, singly_linked_list):
        current = singly_linked_list.head
        while current:
            self.append(current.data)
            current = current.next

    def shift(self, num):
        if num == 0:
            return
        elif num > 0:
            for _ in range(num):
                self.tail.next = self.head
                self.head.prev = self.tail
                self.head = self.head.next
                self.head.prev = None
                self.tail = self.tail.next
                self.tail.next = None
        else:
            for _ in range(abs(num)):
                self.head.prev = self.tail
                self.tail.next = self.head
                self.head = self.head.prev
                self.tail = self.tail.prev
                self.head.prev = None
                self.tail.next = None

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(elements)




# ---------------Test code-----------------
singly_list = LinkedList()
singly_list.append(1)
singly_list.append(2)
singly_list.append(3)
singly_list.append(4)
singly_list.append(5)

doubly_list = DoublyLinkedList()
doubly_list.make_doubly(singly_list)
doubly_list.display()

doubly_list.shift(2)
doubly_list.display()

doubly_list.shift(-1)
doubly_list.display()
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_in_front(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    
    def insert_in_back(self, value):
        new_node = Node(value)
        
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print("None")
    

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete_at_front(self):
        if self.head is None:
            return None
        removed_data = self.head.data
        self.head = self.head.next
        return removed_data

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(current.data)
            current = current.next
        return str(values)
    


    def delete_at_back(self):
        if not self.head:
            return None
        current = self.head
        prev = None
        while current.next:
            prev = current
            current = current.next
        if prev:
            prev.next = None
        else:
            self.head = None
        return current.data


    def search(self, value):
        index = 0
        current = self.head
        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return -1  # Value not found

    def clear(self):
        self.head = None

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def print_forward(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def print_backward(self):
        self._print_backward_helper(self.head)

    def _print_backward_helper(self, node):
        if node is None:
            return
        self._print_backward_helper(node.next)
        print(node.data, end=" ")

    def reverse_recursive(self, node):
        if node.next is None:
            self.head = node
            return
        self.reverse_recursive(node.next)
        temp = node.next
        temp.next = node
        node.next = None

    def reverse(self):
        if not self.head:
            return
        self.reverse_recursive(self.head)

    def reverse_non_recursive(self):
        if not self.head or not self.head.next:
            return
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev



print('-------------(Test Question 1:)-----------------')
linked_list = LinkedList()
linked_list.insert_in_front(3)
linked_list.insert_in_front(2)
linked_list.insert_in_front(1)

print("Initial linked list:")
linked_list.display()

linked_list.insert_in_front(10)

print("Linked list after inserting 10 in front:")
linked_list.display()



print('-------------(Test Question 2:)-----------------')
linked_list = LinkedList()
linked_list.insert_in_back(1)
linked_list.insert_in_back(2)
linked_list.insert_in_back(3)

linked_list.display()

linked_list.insert_in_back(10)

linked_list.display()


print('-------------(Test Question 3:)-----------------')
my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)

print(my_list)

deleted_value = my_list.delete_at_front()
print("Deleted value:", deleted_value)

print(my_list)

print('-------------(Test Question 4:)-----------------')
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)

print("Before Deletion:")
llist.display()

deleted_value = llist.delete_at_back()

print(f"Value Deleted: {deleted_value}")

print("After Deletion:")
llist.display()


print('-------------(Test Question 5:)-----------------')


my_list = LinkedList()
my_list.append(1)
my_list.append(3)
my_list.append(2)
my_list.append(2)

print(my_list.search(1))  # Output: 0
print(my_list.search(2))  # Output: 2


print('-------------(Test Question 6:)-----------------')
list = LinkedList()
list.append(1)
list.append(2)
list.append(3)
list.append(4)
print(list)

list.clear()
print(list)


print('-------------(Test Question 7:)-----------------')
my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
print(my_list.size())


print('-------------(Test Question 8:)-----------------')


my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.print_forward()

print('-------------(Test Question 9:)-----------------')
my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.print_backward()

print()
print('-------------(Test Question 10:)-----------------')

my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)

print("Original list:")
my_list.display()

my_list.reverse()

print("Reversed list:")
my_list.display()

print('-------------(Test Question 11:)-----------------')

linkedList = LinkedList()
linkedList.append(1)
linkedList.append(2)
linkedList.append(3)

print("Original list:")
linkedList.display()

print("Reversed list:")
linkedList.reverse_non_recursive()
linkedList.display()







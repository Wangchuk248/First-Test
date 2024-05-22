# Define a class named Node representing a single node in a singly linked list.
class Node:
    def __init__(self, data): # method for the Node class. Node will have two attributes: data and next.
        self.data = data
        self.next = None
        

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
# Example usage:
# Create an instance of the SinglyLinkedList class.
sll = SinglyLinkedList()
# Append some elements to the linked list.
sll.append(1)
sll.append(2)
sll.append(3)
# Display the elements of the linked list.
sll.display()
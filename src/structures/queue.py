class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class Queue:
    # queue > first in first out list
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """ add node to end of queue """
        if self.tail is None and self.head is None:
            self.tail = self.head = Node(data, None)
            return
        
        self.tail.next_node = Node(data, None)
        self.tail = self.tail.next_node
        return
    
    def dequeue(self):
        """ remove node from top of queue """
        if self.head is None:
            return None
        
        removed = self.head
        self.head = self.head.next_node

        if self.head is None:
            self.tail = None

        return removed

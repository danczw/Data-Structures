class Node:
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node

class Stack:
    # stack > first in last out list
    def __init__(self):
        self.top = None

    def peek(self):
        """ view top of stack """
        return self.top

    def push(self, data):
        """ add to top of stack """
        next_node = self.top
        new_top = Node(data, next_node)
        self.top = new_top
    
    def pop(self):
        """ remove top of stack """
        if self.top is None:
            return
        
        removed = self.top
        self.top = self.top.next_node
        return removed.data

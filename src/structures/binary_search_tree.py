class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

# wrapper class
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def _insert_recursive(self, value, node):
        """ recursively checking left and right node size for insertion """
        if value < node.data:
            
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(value, node.left)

        elif value > node.data:

            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(value, node.right)

        else: # must be duplicate
            return

    def insert(self, value):
        """ insert new data as Node into binary search tree """
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(value, self.root)
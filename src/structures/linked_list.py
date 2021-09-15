class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

# wrapper class
class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def insert_beginning(self, data):
        """ add node to beginning of linked list """
        new_node = Node(data, self.head)

        if self.head is None:
            self.last_node = new_node

        self.head = new_node

    def insert_end(self, data):
        """ add node to end of linked list """
        new_node = Node(data, None)

        if self.head is None:
            self.insert_beginning(data)
            return
        
        self.last_node.next_node = new_node
        self.last_node = new_node

    
    def flatten_arr(self):
        """ flatten list of nodes return array """
        arr = []

        if self.head is None:
            return arr

        node = self.head
        while node:
            arr.append(node.data)
            node = node.next_node
        return arr

    def print_ll(self):
        """ display whole list """
        ll_string = ""
        node = self.head

        if node is None:
            print(None)
        
        while node:
            ll_string += f" {str(node.data)} ->"
            node = node.next_node
        
        ll_string += " None"
        print(ll_string)

    def get_user_by_id(self, user_id):
        """ return user data by id """
        node = self.head

        while node:
            if node.data["id"] is int(user_id):
                return node.data
            
            node = node.next_node
        
        return None

# testing
# ll = LinkedList()

# node4 = Node("data4", ll.head)
# node3 = Node("data3", node4)
# node2 = Node("data2", node3)
# node1 = Node("data1", node2)

# ll.head = node1
# ll.last_node = node4

# ll.insert_beginning("dataBeginningOne")
# ll.insert_end("dataEndOne")

# ll.insert_beginning("dataBeginningTwo")
# ll.insert_end("dataEndTwo")

# ll.print_ll()
import sys

class Node:
    def __init__(self, data):
        self.data = data    # Assign data
        self.next = None    # Initialize next as null

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node.data
            node = node.next

    def insert(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
        else:
            current_node = self.head
            count = 1
            while current_node.next is not None:
                current_node = current_node.next
                count += 1
            current_node.next = node
            
mylist= LinkedList()
try:
    T=int(sys.stdin.readline().rstrip())
    for i in range(T):
        data=int(input())
        head=mylist.insert(data)    
    i = 0
    for elms in mylist:
        if i == 0:
            print(elms, end = '')
        else:
            print(' {}'.format(elms), end = '')
        i += 1
except:
    pass
class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def addNode(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node

    def printLinkedList(self):

        ptr = self.head
        while(ptr):
            print ptr.val,
            ptr = ptr.next
        print


llist = LinkedList()
llist.addNode(9)
llist.addNode(8)
llist.addNode(7)
llist.addNode(6)
llist.addNode(5)
llist.addNode(4)
llist.addNode(3)
llist.addNode(2)
llist.addNode(1)

llist.printLinkedList()

# Qus: https: // practice.geeksforgeeks.org/problems/merge-sort-on-doubly-linked-list/1
# User function Template for python3

"""
# we are using O(1) space
# time complexity is O(nlogn)

"""

'''
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

'''




import sys
def getSecond(head):
    # just check if the provided node is None or not
    if(head == None):
        return head

    # use fast and slow pointer to find the mid of linked list
    slow = head
    fast = head

    while(fast.next and fast.next.next):
        fast = fast.next.next
        slow = slow.next

    # make sure you remove the next reference from slow and prev ref from slow.next
    # node
    temp = slow.next
    slow.next = None  # remember to se the slow.next = None
    if(temp):
        temp.prev = None
    return temp


def mergeList(left, right):

    # just use a dummyNode to avoid any corner case
    dummyNode = Node(-1)
    ptr = dummyNode

    # use same logic to merge two sorted list
    while(left != None and right != None):
        if(left.data < right.data):
            # break node from left and add it to dummy node
            ptr.next = left
            left = left.next
            if(left):  # remove the back reference of new left node
                left.prev = None

        else:
            ptr.next = right
            right = right.next
            if(right):  # remove the right reference of new left node
                right.prev = None

        # we need to remove next reference
        temp = ptr
        ptr = ptr.next

        if(ptr):
            ptr.prev = temp  # add prev reference to new node added to list
            ptr.next = None

    if(left != None):
        ptr.next = left
        ptr.next.prev = ptr  # add prev reference

    if(right != None):
        ptr.next = right
        ptr.next.prev = ptr  # add prev reference

    nHead = dummyNode.next  # we need to remove this back reference of dummy node
    # so that we can avoid the -1 value in dummy node
    nHead.prev = None
    return nHead


# Function to sort the given doubly linked list using Merge Sort.
def sortDoubly(head):
    # if head is None or head.next is none then it means list is alreay sorted
    # so return head

    if(head == None or head.next == None):
        return head

    # now find the mid point let say both list are different
    # make sure to remove any reference to prev and next pointer while doing so
    first = head
    second = getSecond(head)

    # print(first.data,second.data)

    leftSorted = sortDoubly(first)  # divide
    rightSorted = sortDoubly(second)  # divide

    head = mergeList(leftSorted, rightSorted)

    return head

# {
#  Driver Code Starts
# Initial Template for Python 3


sys.setrecursionlimit(1000000)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def printList(self, node):
        while(node.next is not None):
            node = node.next
        while node.prev is not None:
            node = node.prev
        while(node is not None):
            print(node.data, end=" ")
            node = node.next
        print()


def printList(node):
    temp = node

    while(node is not None):
        print (node.data, end=" ")
        temp = node
        node = node.next
    print()
    while(temp):
        print (temp.data, end=" ")
        temp = temp.prev


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        llist = DoublyLinkedList()
        for e in arr:
            llist.append(e)
        llist.head = sortDoubly(llist.head)
        printList(llist.head)
        print()


# } Driver Code Ends

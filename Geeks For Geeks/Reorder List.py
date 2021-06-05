# Qus:https://practice.geeksforgeeks.org/problems/reorder-list/1
# time complexity O(N)
# space complexity O(1)

# User function Template for python3
import sys
sys.setrecursionlimit(6500)
'''
# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None
'''

'''
# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
'''


def findMid(root):

    slow = head
    fast = head

    while(fast.next and fast.next.next):
        fast = fast.next.next
        slow = slow.next

    temp = slow.next
    slow.next = None
    return temp


def reverse(root):

    if(root == None):
        return root

    if(root.next == None):
        return root

    newHead = reverse(root.next)

    root.next.next = root
    root.next = None

    return newHead


def reorderList(self):
    if (self.head == None or self.head.next == None):
        return self.head

    first = self.head
    second = findMid(self.head)

    second = reverse(second)

    ptr1 = first
    ptr2 = second

    while(first and ptr2):

        # store next value of second
        temp = ptr2.next
        ptr2.next = first.next
        first.next = ptr2

        # move pointers forward
        first = first.next.next
        ptr2 = temp

    return first


# {
#  Driver Code Starts
# Initial Template for Python 3

# Node Class
class node:
    def __init__(self, val):
        self.data = val
        self.next = None

# Linked List Class


class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head == None:
            self.head = node(val)
            self.tail = self.head
        else:
            new_node = node(val)
            self.tail.next = new_node
            self.tail = new_node

    def createList(self, arr, n):
        for i in range(n):
            self.insert(arr[i])
        return self.head

    reorder_List = reorderList

    def printList(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.data, end=" ")
            tmp = tmp.next
        print()


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        lis = Linked_List()
        head = lis.createList(arr, n)
        lis.reorder_List()
        lis.printList()

# } Driver Code Ends

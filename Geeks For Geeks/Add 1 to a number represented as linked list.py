# Qus:https://practice.geeksforgeeks.org/problems/add-1-to-a-number-represented-as-linked-list/1
# User function Template for python3
import sys
sys.setrecursionlimit(1500)

'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''


def getCarry(head):

    if(head == None):
        return 0

    c = 0

    if(head.next):
        c = getCarry(head.next)
        if(head.data + c == 10):
            head.data = 0
            c = 1
            return c
        else:
            head.data += c
        return 0
    else:
        if(head.data == 9):
            head.data = 0
            c = 1
        else:
            head.data += 1
        return c


class Solution:
    def addOne(self, head):
        # Returns new head of linked List.

        c = getCarry(head)

        if(c):

            newNode = Node(c)
            newNode.next = head
            head = newNode

        return head


# {
#  Driver Code Starts
# Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next


def PrintList(head):
    while head:
        print(head.data, end='')
        head = head.next


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        num = input()
        ll = LinkedList()  # create a new linked list 'll1'.
        for digit in num:
            ll.insert(int(digit))  # add to the end of the list

        resHead = Solution().addOne(ll.head)
        PrintList(resHead)
        print()


# } Driver Code Ends

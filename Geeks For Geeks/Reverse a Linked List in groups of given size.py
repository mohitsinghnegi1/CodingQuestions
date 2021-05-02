# Qus:https://practice.geeksforgeeks.org/problems/reverse-a-linked-list-in-groups-of-given-size/1
# easiest way possible

"""Return reference of new head of the reverse linked list
  The input list will have at least one element
  Node is defined as

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
  This is method only submission.
  You only need to complete the method.
"""


class Solution:
    def reverse(self, head, k):
        # Code here

        # reverse a linked list using iterative method

        prev = None
        ptr = head
        next1 = None
        c = 0  # to keep track of how many nodes to reverse
        while(ptr and c < k):  # c<k bec we need prev which is end of reversed k nodes
            # now we need to reverse the direction of next pointer
            # so we need a pointer to next node for reference later
            # Remember we are reversing the next pointer of current node
            next1 = ptr.next

            ptr.next = prev
            prev = ptr
            ptr = next1
            c += 1

        if(ptr != None):
            # we know if ptr!=None we need to reverse next k nodes
            # and set next of current head as (result of next reversal)
            head.next = self.reverse(ptr, k)

        # first reversal head
        return prev


# {
#  Driver Code Starts
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        # self.tail

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            # arr.append(str(temp.data))
            temp = temp.next
        print()


if __name__ == '__main__':
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n = input()
        values = list(map(int, input().split()))
        for i in reversed(values):
            llist.push(i)
        k = int(input())
        new_head = LinkedList()
        ob = Solution()
        new_head = ob.reverse(llist.head, k)
        llist.head = new_head
        llist.printList()
        t -= 1


# } Driver Code Ends

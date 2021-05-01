

# infix to posfix conversion : https://www.youtube.com/watch?v=PAceaOSnxQs
# how to evaluate postfix expression (using stack pop when you get operator, in case of divide pop 2 elemnt a,b
#  the operand which poped last ie b will be b/a)
# https://www.youtube.com/watch?v=84BsI5VJPq4


# User function Template for python3
from collections import deque
from collections import OrderedDict

'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

# Function to return a list containing elements of left view of the binary tree.


def LeftView(root):
    if(root == None):
        return []

    d = OrderedDict()

    queue = deque([])
    queue.append((root, 0))

    while(queue):
        node, level = queue.popleft()
        if(level not in d):
            d[level] = node.data
        if(node.left):
            queue.append((node.left, level+1))
        if(node.right):
            queue.append((node.right, level+1))

    return d.values()

    # code here


# {
#  Driver Code Starts
# Contributed by Sudarshan Sharma
# Tree Node


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree


def buildTree(s):
    # Corner Case
    if(len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size+1

    # Starting from the second element
    i = 1
    while(size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size-1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if(currVal != "N"):

            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size+1
        # For the right child
        i = i+1
        if(i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if(currVal != "N"):

            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size+1
        i = i+1
    return root


if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        root = buildTree(s)
        result = LeftView(root)
        for value in result:
            print(value, end=" ")
        print()

# } Driver Code Ends

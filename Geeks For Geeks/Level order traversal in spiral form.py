# Qus:https://practice.geeksforgeeks.org/problems/level-order-traversal-in-spiral-form/1
# User function Template for python3

"""
Timecomplexity is O(n)

"""
# Function to return a list containing the level order traversal in spiral form.
from collections import deque


def findSpiral(root):
    # Code here

    if(root == None):
        return []

    stack1 = [root]
    stack2 = []
    out = []
    while(stack1 or stack2):

        while(stack1):
            node = stack1.pop()
            # print(node.data,end='')
            out.append(node.data)
            if(node.right):
                stack2.append(node.right)
            if(node.left):
                stack2.append(node.left)

        while(stack2):
            node = stack2.pop()
            # print(node.data,end='')
            out.append(node.data)
            if(node.left):
                stack1.append(node.left)
            if(node.right):
                stack1.append(node.right)

    return out


# {
#  Driver Code Starts
# Initial Template for Python 3
# Initial Template for Python 3
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
        result = findSpiral(root)
        for value in result:
            print(value, end=" ")
        print()


# } Driver Code Ends

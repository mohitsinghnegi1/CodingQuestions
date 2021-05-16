# Qus:https://practice.geeksforgeeks.org/problems/lowest-common-ancestor-in-a-binary-tree/1#

# User function Template for python3

'''
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''
from collections import deque


def findlca(root, n1, n2):

    if(root == None):
        return [0, None]

    count = 0

    if(root.data in [n1, n2]):
        count += 1

    a, lc = findlca(root.left, n1, n2)
    b, lc1 = findlca(root.right, n1, n2)

    if(a == 2):
        return [2, lc]
    if(b == 2):
        return [2, lc1]

    if(count == 1):

        if(a == 1):
            return [2, root]
        if(b == 1):
            return [2, root]
        return [1, root]
    else:
        if(a == 1 and b == 1):
            return [2, root]

        if(a == 1):
            return [1, lc]
        if(b == 1):
            return [1, lc1]
        return [0, None]


class Solution:
    # Function to return the lowest common ancestor in a Binary Tree.
    def lca(self, root, n1, n2):
        # Code here

        if(root == None):
            return None

        return findlca(root, n1, n2)[1]


# {
#  Driver Code Starts
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
        a, b = list(map(int, input().split()))
        s = input()
        root = buildTree(s)
        k = Solution().lca(root, a, b)
        print(k.data)


# } Driver Code Ends

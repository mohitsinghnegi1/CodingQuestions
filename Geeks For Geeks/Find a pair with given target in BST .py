# Qus:https://practice.geeksforgeeks.org/problems/find-a-pair-with-given-target-in-bst/1#

# using two pointer in O(n) and O(n) space
# {
# Driver Code Starts
# Initial Template for Python 3
from collections import deque
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

 # } Driver Code Ends
# User function Template for python3


'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

'''


class Solution:

    def __init__(self):
        self.inorderList = []

    def inorder(self, root):

        if(root == None):
            return

        self.inorder(root.left)
        self.inorderList.append(root.data)
        self.inorder(root.right)

    def getPairs(self, target):
        l = 0
        r = len(self.inorderList)-1

        while(l < r):

            sum1 = self.inorderList[l] + self.inorderList[r]

            if(sum1 == target):
                return 1
            elif(sum1 < target):
                l += 1
            else:
                r -= 1
        return 0

    # root : the root Node of the given BST
    # target : the target sum
    def isPairPresent(self, root, target):
        # code here.

        if(root == None):
            return self.ans

        self.inorder(root)

        # print(self.inorderList)

        return self.getPairs(target)


# {
# Driver Code Starts.
if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        summ = int(input())
        root = buildTree(s)
        print(Solution().isPairPresent(root, summ))
# } Driver Code Ends


# 2nd approach using hash map

# {
# Driver Code Starts
# Initial Template for Python 3
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

 # } Driver Code Ends
# User function Template for python3


'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

'''


class Solution:

    def __init__(self):
        self.ans = 0
        self.d = {}

    def countPairsWithTargetSum(self, root, target):

        if(root == None):
            return

        if((target - root.data) in self.d):
            self.ans = 1

        self.d[root.data] = True

        self.countPairsWithTargetSum(root.left, target)
        self.countPairsWithTargetSum(root.right, target)

    # root : the root Node of the given BST
    # target : the target sum
    def isPairPresent(self, root, target):
        # code here.

        if(root == None):
            return self.ans

        self.countPairsWithTargetSum(root, target)

        return self.ans


# {
# Driver Code Starts.
if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        summ = int(input())
        root = buildTree(s)
        print(Solution().isPairPresent(root, summ))
# } Driver Code Ends

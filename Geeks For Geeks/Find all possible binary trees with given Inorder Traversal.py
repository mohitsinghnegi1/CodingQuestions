# Qus:https://www.geeksforgeeks.org/find-all-possible-trees-with-given-inorder-traversal/
# Python program to find binary tree with given
# inorder traversal

# Node Structure
class Node:

    # Utility to create a new node
    def __init__(self, item):
        self.key = item
        self.left = None
        self.right = None

# A utility function to do preorder traversal of BST


def preorder(root):
    if root is not None:
        print root.key,
        preorder(root.left)
        preorder(root.right)


# Function for constructing all possible trees with
# given inorder traversal stored in an array from
# arr[start] to arr[end]. This function returns a
# vector of trees.
def getTrees(arr, start, end):

    if(start > end):
        return [None]
    trees = []

    for i in range(start, end+1):

        # ith node will be the root node

        leftInorderSubtrees = getTrees(arr, start, i-1)
        rightInorderSubtrees = getTrees(arr, i+1, end)

        for leftInorderSubtree in leftInorderSubtrees:
            for rightInorderSubtree in rightInorderSubtrees:

                root = Node(arr[i])
                root.left = leftInorderSubtree
                root.right = rightInorderSubtree
                trees.append(root)
    return trees


# Driver program to test above function
inp = [4, 5, 7]
n = len(inp)

trees = getTrees(inp, 0, n-1)

print "Preorder traversals of different possible\
Binary Trees are "
for i in trees:
    preorder(i)
    print ""

# This program is contributed by Nikhil Kumar Singh(nickzuck_007)

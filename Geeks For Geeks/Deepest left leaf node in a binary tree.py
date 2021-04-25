# Python program to find the deepest left leaf in a given
# Binary tree

# A binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# A wrapper for left and right subtree


def deepestLeftLeaf(root, l=0, left=False):

    if(root == None):
        return None
    if(root.left == None and root.right == None):
        # leaf node
        if(left):
            return {'level': l, 'val': root.val}
        return None

    a = deepestLeftLeaf(root.left, l+1, left=True)
    b = deepestLeftLeaf(root.right, l+1, left=False)

    res = None
    if(a):
        res = a
    if(b):
        if(res == None):
            res = b
        else:
            if(res['level'] < b['level']):
                res = b
    return res


# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.right = Node(7)
root.right.right.right = Node(8)
root.right.left.right.left = Node(9)
root.right.right.right.right = Node(10)

result = deepestLeftLeaf(root)

if result is None:
    print "There is not left leaf in the given tree"
else:
    print "The deepst left child is", result['val']

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)

# Qus:https://leetcode.com/problems/serialize-and-deserialize-bst/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        global s
        s = ""

        def preorder(root):
            global s
            if(root == None):
                s += '#,'
                return
            s += str(root.val)+','
            preorder(root.left)

            preorder(root.right)

        preorder(root)

        return s[:-1]

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        print "data", data

        itr = iter(data.split(','))

        def preorder(itr):

            val = itr.next()
            if(val == '#'):
                return None

            root = TreeNode(val)
            root.left = preorder(itr)

            root.right = preorder(itr)

            return root

        return preorder(itr)


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans

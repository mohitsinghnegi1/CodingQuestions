# QUs:https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# Remember only preorder will work in this 
# time complexity O(n)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        #Intution behind serialize
        # do preorder traversal
        # if node val==None add '#'
        # else add node.val to vals 
        # and move to its left then right
        # at the end return the join of this list

        def preorder(root):
            if(root==None):
                vals.append('#')
                return
            
            vals.append(str(root.val))
            preorder(root.left)
            preorder(root.right)
            
        vals=[]
        
        preorder(root)
        
        return " ".join(vals)
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # Intution behind deserialize
        # Use Iter (New Learning) to triverse in string array
        # do preorder triversal again 
        # instead of extracting val we are construction a tree from the given val
        # (ie reverse process) 

        def decodeIt():
            val=itr.next()
            if(val=='#'):
                return None
            node=TreeNode(val)
            node.left=decodeIt()
            node.right=decodeIt()
            
            return node
        
        itr=iter(data.split(' '))
        
        root=decodeIt()# assuming it will return a TreeNode
        
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
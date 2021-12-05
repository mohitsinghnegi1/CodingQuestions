# Qus:https://leetcode.com/problems/house-robber-iii/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def solve(node,d):
            
            # print depth*'*'
            
            
            
            
            if(node==None):
                return 0
            
            if(d.get(node,False)!=False):
                return d[node]
            
            leftLeft = 0
            leftRight = 0
            if(node.left):
                leftLeft = solve(node.left.left,d)
                # if(node.val==4):
                #     print "for 4 left left",leftLeft,node.left.left.val
                
                leftRight = solve(node.left.right,d)

            rightLeft = 0
            rightRight = 0
            if(node.right):
                rightLeft = solve(node.right.left,d)
                rightRight = solve(node.right.right,d)
            
            rootAns = node.val + leftLeft  + leftRight + rightLeft + rightRight
            
            # print "rootAns",rootAns,node.left.left.val if node.left and node.left.left else 0
            
            rootLeftAns = solve(node.left,d)
            rootRightAns = solve(node.right,d)
            # print "=>",max(rootAns,rootLeftAns+rootRightAns), "when => ",node.val
            
            
            d[node] = max(rootAns,rootLeftAns+rootRightAns)
            
            return d[node]
            
        d = {}
        return solve(root,d)
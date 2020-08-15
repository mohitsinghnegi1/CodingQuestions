# QUs :https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

def bfs(root):
    
    queue=[]
    queue.append(root)
    while(queue):
        v=[]

        # process all same level elemnt first ans insert child in v array
        # pop out top elemnt from queue and point its next to first elemnt at queue if             # available
        while(queue):
            node=queue.pop(0)
            if(queue):
                node.next=queue[0]
            if(node.left):
                v.append(node.left)

            if(node.right):
                v.append(node.right)
      
        
        queue.extend(v)


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if(root==None):
            return root
        #first idea is modified BFS
        bfs(root)
        return root
    
# Qus:https://leetcode.com/problems/copy-list-with-random-pointer/

"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if(head==None):
            return None
        
        ptr=Node(0)
        head1=ptr
        d={}
        
        
        p=head
        while(p!=None):
            
            if(p in d):
                ptr.next=d[p]
            else:
                #this condition is possible when we have already created a node due
                # some other node 's rendom pointer pointing to this node
                ptr.next=Node(p.val)
                #store node as a key in dict and copied node in value
                d[p]=ptr.next
            
            if(p.random in d):
                # if rendom node already exist then just point cur 's rendom to that                 # node
                d[p].random=d[p.random]
                
            else:
                #in case random node is not present then add that random node 
                #and create a new node to store it as a value to that random node
                #point cur 's random to that node
                if(p.random==None):
                    d[p].random=None
                else:
                    d[p.random]=Node(p.random.val)
                    d[p].random=d[p.random]
            
            ptr=ptr.next
            p=p.next
              
        
        return head1.next
        
        
            
        
        
        
# Qus:https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
# complexity O(n)
# space complexity 0(1)


class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        cur=head
        while(cur!=None):
            #if cur.child not equal to null means we need to flattern the node
            if(cur.child):
                # tail node will point to the last node of child linked list
                tail=cur.child
                #trivered to the end of child linked list
                while(tail.next):
                    tail=tail.next
                #break the link list from cur position and add the new child linked list in                       #between
                tail.next=cur.next
                #check if next node cur node is not equal to null
                if(tail.next):
                    tail.next.prev=tail
                cur.next=cur.child
                cur.next.prev=cur
                #it is important to set child to the null as per the qus
                cur.child=None
                
            #move to next node after flaterning the node (ie adding child in front and setting 
            # child as null)
            cur=cur.next
        
        return head

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

#solution using stack data structur
# complexity O(n) and O(n) space complexity

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        #intution we are just doing dfs creating a new linked list by using extra space
        
        if(head==None):
            return
        
        cur=head
        stack=[]
        stack.append(cur)
        newHead=Node()
        ptr=newHead
        
        while(stack):
            nextNode = stack.pop()
            ptr.next = nextNode
            ptr.next.prev = ptr
            ptr=ptr.next
            
            # add ptr.next node into stack first so that we access node in dfs manner
            if(ptr.next):
                stack.append(ptr.next)
                
            # see if there is any child or not ,if yes then add that node into stack
            if(ptr.child):
                stack.append(ptr.child)
            
            #need to set ptr.child as None 
            ptr.child=None
            
        # first node prev should be None also
        newHead.next.prev=None
        return newHead.next
            
        
        
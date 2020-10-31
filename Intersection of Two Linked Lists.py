# Qus:https://leetcode.com/problems/intersection-of-two-linked-lists/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # case like [1]  and []  no intersection point
        if(headA==None or headB==None):
            return None
        
        #intution 
        # first triverse in 1 linked list then redirect it to 2nd linked list and if there
        # is any interection then it will surely intersect otherwise it will not so thats 
        # why we need an extra flag to check if we have triversed both linked list but
        # have not got that interection point so in that case also we will return None
        
        ptr1=headA
        ptr2=headB
        flag1=False
        flag2=False
        
        while(ptr1!=ptr2):
            
            #check if we have triversed both list
            if(ptr1.next==None and flag1==True or ptr2.next==None and flag2==True):
                return None
        
            # if we are at the end of first linked list then redirect it to second linked list
            if(ptr1.next==None):
                ptr1=headB
                flag1=True
            else:
                ptr1=ptr1.next
            # same redirection as above 
            if(ptr2.next==None):
                ptr2=headA
                flag2=True
            else:
                ptr2=ptr2.next
                
        # return the intersection node
        return ptr1
# QUs:https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #create a dummy node
        root=ListNode(-1)
        
        ptr=root
        
        sum1=0
        c=0
        
        while(l1!=None and l2!=None):
            
            #sum is equal to sum of both node
            sum1=l1.val+l2.val
            #modulo will be stored in new node Note we need to add carry too
            n=(sum1+c)%10
            #cal carry which will be transferred to the next node
            c=(sum1+c)/10
            ptr.next=ListNode(n)
            
            #move to the next node
            ptr=ptr.next
            l1=l1.next
            l2=l2.next
        
        # if 1st list is a long list
        while(l1):
            n=(l1.val+c)%10
            c=(l1.val+c)/10
            ptr.next=ListNode(n)
            l1=l1.next
            ptr=ptr.next
        
        #if 2nd list is a long list
        while(l2):
            n=(l2.val+c)%10
            c=(l2.val+c)/10
            ptr.next=ListNode(n)
            l2=l2.next
            ptr=ptr.next
        
        #make sure if c is not zero then create an additional node to store it
        if(c):
            ptr.next=ListNode(c)
        
        return root.next
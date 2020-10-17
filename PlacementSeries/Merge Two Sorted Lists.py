# Qus:https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ptr1=l1
        ptr2=l2
        #just create a dummy node to make solution easy
        ptr3=ListNode(-1)
        head=ptr3
        
        while(l1!=None and l2!=None):
            if(l1.val<=l2.val):
                ptr3.next=l1
                l1=l1.next
                ptr3=ptr3.next
                ptr3.next=None
            else:
                ptr3.next=l2
                l2=l2.next
                ptr3=ptr3.next
                ptr3.next=None
        
        if(l1!=None):
            ptr3.next=l1
        if(l2!=None):
            ptr3.next=l2
            
        
        return head.next
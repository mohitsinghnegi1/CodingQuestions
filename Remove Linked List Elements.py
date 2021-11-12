# Qus:https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummyhead = ListNode()
        
        ptr = dummyhead
        ptr2 = head
        while(ptr2):
            while(ptr2 and ptr2.val!=val):
                ptr.next = ptr2
                ptr2 = ptr2.next
                ptr=ptr.next
                ptr.next=None

            while(ptr2 and ptr2.val==val):
                ptr2 = ptr2.next

            
        return dummyhead.next
            
        
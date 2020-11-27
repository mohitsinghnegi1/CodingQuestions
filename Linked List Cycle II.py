# Qus:https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head

        while(fast != None and fast.next != None):

            slow = slow.next
            fast = fast.next.next

            if(slow == fast):
                break

        # What if there is no cycle
        if(fast == None or fast.next == None):
            return None

        slow = head
        while(slow != fast):
            slow = slow.next
            fast = fast.next
        return slow

        '''
            Proof
            *****
            https://www.youtube.com/watch?v=QfbOhn0WZ88
            
            Head--(Dist l1)-----IntersectionPoint---(Dist l2)---->MeetingPoint
                                      |__________________________________|
                                      
            Distance covered by slow pointer = L1+L2  (this l2 will be any number of                   rounds that slow pointer have covered after it comes inside the cycle)
            
            Distance covered by fast pointer = L1+l2+nC # where n denotes num
            slow=2fast
            L1+l2 = L1+L2+nC
            2(L1+L2)=L1+L2+nC
            L1=nC-L2 
        
        
        '''

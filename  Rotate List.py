# Qus:https://leetcode.com/problems/rotate-list/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # intution
        # just break and add

        # if len is 0
        if(k == 0 or head == None or head.next == None):
            return head

        ptr = head
        length = 0

        while(ptr != None):
            length += 1
            ptr = ptr.next

        # remeber the corner case : when k>lenght
        k = k % length
        # corner case
        if(k == 0):
            return head

        moves = length-k

        temp = None
        ptr = head
        while(moves > 1):
            ptr = ptr.next
            moves -= 1
        temp = ptr.next
        ptr.next = None

        # move
        ptr = temp
        while(ptr and ptr.next != None):
            ptr = ptr.next
        ptr.next = head
        head = temp
        return head

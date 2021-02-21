
# Qus:https://leetcode.com/problems/odd-even-linked-list/


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # case if there are 2 or less node then return
        if(head == None or head.next == None or head.next == None):
            return head

        # keep ptr1 at odd position
        ptr1 = head

        # keep ptr2 at even position
        ptr2 = head.next

        # this pointer will be use as a ptr1's next node
        temp = head.next

        while(ptr1.next != None and ptr1.next.next != None):

            # point ptr1.next in next odd position and move ptr1 at that position
            ptr1.next = ptr1.next.next
            ptr1 = ptr1.next

            # check if ptr2.next.next location is not None
            # if that's the case then set its next as None
            # bec it will be the last even node
            if(ptr2.next == None or ptr2.next.next == None):
                ptr2.next = None
                break

            # if next even position is available the set ptr2.next to that node
            # move ptr2 to that node
            ptr2.next = ptr2.next.next
            ptr2 = ptr2.next
            #print ptr2.val

        # at the end assign pt1.next to that 2nd node
        ptr1.next = temp

        return head

        # end time solution >>>>>>>>>>>>>>
        # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(head == None or head.next == None):
            return head

        temp = head.next
        ptr = head  # used to update odd
        ptr2 = temp

        i = 0
        while(ptr.next and ptr.next.next):
            ptr.next = ptr.next.next
            ptr = ptr.next
            ptr2.next = ptr2.next.next
            ptr2 = ptr2.next

        ptr.next = temp
        return head

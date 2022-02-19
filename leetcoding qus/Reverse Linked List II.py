# Qus: https: // leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        # in case there is only one node , return the head
        if(m == n):
            return head

        # reverse the node from m to n
        def reverse(count, ptr, n):

            prev = None
            mid = ptr
            temp = ptr
            while(count < n):

                temp = mid.next
                mid.next = prev
                prev = mid
                mid = temp
                count += 1

            return mid, prev

        count = 0
        # add one extra node in front for ease
        head1 = ListNode()
        head1.next = head

        ptr = head1

        # proceed up to m-2 steps
        while(count < m-1):
            ptr = ptr.next
            count += 1

        frontNode = ptr  # node just before m
        nextNode = ptr.next

        # assume that this will rerse the direction on pointer
        last, next1 = reverse(count, ptr.next, n)

        frontNode.next = next1  #
        nextNode.next = last  # imagine it by example

        return head1.next

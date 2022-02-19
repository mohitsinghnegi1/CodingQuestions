# Qus:https://leetcode.com/problems/reorder-list/

# time complexity n**2  (TLE)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        """
        Intutution :
        
            -> 1 2 3 4
            -> 1 4 3 2
            -> 1 4 2 3
            -> 1 4 2 3

        """

        # function which will reverse the llinked list and return the head after reverse
        def reverse(head):

            if(head == None):
                return head

            if(head.next == None):
                return head

            last = reverse(head.next)

            head.next.next = head
            head.next = None

            return last

        # function to move one node forward
        def oneStep(head):
            if(head == None):
                return

            ptr = head.next
            head.next = reverse(ptr)  # the reverse list will be next of head
            # then again move one step ahead and repeat same
            oneStep(head.next)

        oneStep(head)


# timecomplexity O(N) somhow passed

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution2(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        """
        Intution 
        1. divide linked list into 2 list (find middle of linked list)
        2. reverse the second list 
        3. merge the two lists
    
        """

        slow, fast = head, head

        while(fast.next and fast.next.next):

            fast = fast.next.next
            slow = slow.next

        head1 = head  # [ 1,2,3]
        head2 = slow.next  # [ 4, 5]
        slow.next = None

        # reverse linked list

        def reverse(head):
            if(head == None):
                return head
            if(head.next == None):
                return head

            last = reverse(head.next)
            head.next.next = head
            head.next = None

            return last

        head2 = reverse(head2)  # [5 , 4]

        # print head2

        # merge these two list

        def merge(head1, head2):
            if(head1 == None):
                return head1
            temp = head1.next
            head1.next = head2
            merge(head2, temp)

        merge(head1, head2)

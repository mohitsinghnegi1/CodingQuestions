# Qus:https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def reverse(head1, head):

    if(head1.next == None):
        head = head1
        return head, head1

    head, nextNode = reverse(head1.next, head)

    nextNode.next = head1
    head1.next = None

    return [head, head1]


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if(head == None):
            return head

        newHead = None    # This will be the pointer to the first Node in new List
        first = head      # this will be pointing to first node within K nodes group
        last = head       # this will be pointing to last node within K nodes group
        prev = None       # prev will we used to link the last node of previously reversed                           # group to the first of new reversed group
        count = 0         # count will be used to track the node count
        temp = None       # temp will be used to keep the next node of last before reversal

        # move until last so that we get the exact count of nodes, and process all nodes
        while(last):

            count += 1

            # in case we are at the end of each K group we need to swap list
            # from first to last
            if(count % k == 0):

                temp = last.next
                # set last.next to None so that we get a proper group of K,avoid cycle
                last.next = None
                # revering will give us the first and the last node of reversed
                # linked list
                first, last = reverse(first, first)

                # see if this is first time reverse , set the newHead
                if(prev == None):

                    newHead = first
                    prev = last  # last will be the prev , the prev will will use
                    # to link next reversed group of K
                else:
                    # if this is not the first K group reversal
                    # then link prev with this first node of reversed K group
                    prev.next = first
                    # once it is linked set the prev to last
                    prev = last

                # now move to the next without setting link
                # we will link after next k group reversal
                first = last = temp
            else:
                # in case count % k !=0 increment last
                last = last.next

        # special case to handle the nodes which we dont need to reverse (nodes < K)
        if(count % k != 0):
            # if the number of nodes less then k in the linked list , then
            # just return the old list
            if(count < k):
                return head
            # else we know that prev will be there
            # and temp will carry the first node
            # we need to declare these two variable as a gloabl variable
            prev.next = temp

        return newHead

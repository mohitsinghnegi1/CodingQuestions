# Qus:https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# time complexity O(N) and space complexity O(1)
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


# easy way recursion
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def reverse(head, count, k):

    if(count < k):
        return head
    # reverse a linked list using iterative method

    prev = None
    ptr = head
    next1 = None
    c = 0  # to keep track of how many nodes to reverse
    while(ptr and c < k):  # c<k bec we need prev which is end of reversed k nodes
        # now we need to reverse the direction of next pointer
        # so we need a pointer to next node for reference later
        # Remember we are reversing the next pointer of current node
        next1 = ptr.next

        ptr.next = prev
        prev = ptr
        ptr = next1
        c += 1

    count -= c

    if(ptr != None):
        # we know if ptr!=None we need to reverse next k nodes
        # and set next of current head as (result of next reversal)
        head.next = reverse(ptr, count, k)

    # first reversal head
    return prev


class Solution(object):
    def reverseKGroup(self, head, k):

        ptr = head
        count = 0
        while(ptr):
            count += 1
            ptr = ptr.next

        # keep track of count so that we don't reverse the last remaining part
        return reverse(head, count, k)


#  Easiest way using pure recursion -> with my thought

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def reverse(head):

    if(head.next == None):
        return head

    newHead = reverse(head.next)
    head.next.next = head

    return newHead


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        """
        Intution : first reverse the last slot return reversed head
        2. then reverse the current slot of k node as new Head
        3. set the current head = reverseHead 
        return new head
        In case there is no enough nodes return head
        
        How to approach 
        crete a linked list of 7 nodes assume k as 2 then try to do above algo
        """

        count = 0
        prev = None
        next1 = head
        while(next1 != None and count < k):
            count += 1
            prev = next1
            next1 = next1.next

        if(count < k):
            return head

        revHead = self.reverseKGroup(next1, k)

        # reverse the cur par ,
        prev.next = None

        newHead = reverse(head)
        head.next = revHead

        return newHead

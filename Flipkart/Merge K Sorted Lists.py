# Qus:https://www.interviewbit.com/problems/merge-k-sorted-lists/
"""
Intution :
    use the concept of merge sort 

    check the min of all the linked list ptr value , keep on constructing the resultant linked list

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


from heapq import heapush,heappop
class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):

        dummyHead = ListNode(-1)
        ptr2 = dummyHead

        while(True):
            minPtr = None
            index = 0
            for i in range(len(A)):
                ptr = A[i]
                if(ptr!=None):
                    if(minPtr==None):
                        minPtr = ptr
                        index = i
                        
                    else:
                        # minPtr = ptr if ptr.val < minPtr.val else minPtr
                        if(ptr.val < minPtr.val):
                            minPtr = ptr
                            index = i

            if(minPtr== None):
                break
            A[index] = A[index].next
            ptr2.next = minPtr
            ptr2 = ptr2.next 
            ptr2.next = None
                
                
        return dummyHead.next

# we need to optimise this solution using heap

from heapq import heappush, heappop
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None



class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):

        dummyHead = ListNode(-1)
        ptr2 = dummyHead

        heap = []
        for i in range(len(A)):
            ptr = A[i]
            if(ptr!=None):
                heappush(heap,(ptr.val,ptr))
        


        while(heap):
            val,ptr = heappop(heap)
            ptr2.next = ptr
            ptr2 = ptr2.next
            if(ptr.next):
                heappush(heap,(ptr.next.val,ptr.next))
            ptr2.next = None 

        return dummyHead.next


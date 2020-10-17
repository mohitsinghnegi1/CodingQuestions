# QUs: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

#two pass solution O(N)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        size=0
        ptr=head
        while(ptr):
            size+=1
            ptr=ptr.next
        
        n=size-n
        
        if(n==0):
            #if node to delete is a first node the just return head.next
            return head.next
        
        count=0
        ptr1=head
        while(True):
            count+=1
            
            if(count==n):
                temp=ptr1.next
                ptr1.next=ptr1.next.next
                temp.next=None
                return head
            
            ptr1=ptr1.next


#need one pass solution
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        #Intution
        #maintain a gab of n and once ptr2 comes to the end delete the node
        #initially gap is set to 1 bec ptr2=head and ptr1=None
        gap=1
        ptr1=None
        ptr2=head
        
        while(ptr2.next):
            
            if(gap>=n):
                if(ptr1==None):
                    ptr1=head
                else:
                    ptr1=ptr1.next
                
            ptr2=ptr2.next
            gap+=1
        
        #if it is node 1
        if(ptr1==None):
            return head.next
        
        temp=ptr1.next
        #remove node
        ptr1.next=ptr1.next.next
        #detach nth node from the last
        temp.next=None
        
        return head
        
        
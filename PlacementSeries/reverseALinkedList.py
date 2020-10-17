# Qus:https://leetcode.com/problems/reverse-linked-list/submissions/



#Recursive approach time complexity O(n)
def reverse(root):
    
    
    if(root.next==None):
        #if it is a last node simply return it
        return root
    
    next1=reverse(root.next)
    
    #reverse the next pointer of the next node. ie (  cur ->next-> to cur <-next   )
    root.next.next=root
    root.next=None

    #always return the last node
    return next1


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        
        """
        if(head==None):
            return None
        
        ptr1=head
        
        #this function will return last node of linked list
        return reverse(ptr1)
        


#iterative approach
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if(head==None or head.next==None):
            return head
        
        #Intution
        #just reverse the arrow of each node 
        #keep in mind that we need to store the next node in temp 
        #before reversing then next of cur node
        #keep ptr1=None in the begining as we are not touching
        #ptr1 in the sence of reversing a node
        #once cur.next is reverse move each node by one step time complexity O(n)
        #at the end ptr2 will become none
        #we need to return then ptr1 node as it will be pointing to the last
        #node at the end
        
        
        ptr1=None
        ptr2=head
        
        while(ptr2):
            
            temp=ptr2.next
            ptr2.next=ptr1
            
        
            ptr1=ptr2
            ptr2=temp
            
        return ptr1
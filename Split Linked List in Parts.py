# Qus:https://leetcode.com/problems/split-linked-list-in-parts/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        count = 0
        ptr = root
        while(ptr != None):
            count += 1
            ptr = ptr.next

        nodes = count/k
        r = count % k

        def getNodes(ptr, nodes):
            if(nodes == 0):
                return None, ptr

            lnode = ptr
            c = 0

            while(ptr != None and c < nodes):

                if(c == nodes-1):
                    temp = ptr.next
                    ptr.next = None
                    ptr = temp
                    break

                ptr = ptr.next
                c += 1

            return lnode, ptr

        # print nodes,r
        out = []

        count = 0
        ptr = root
        while(count < k):
            if(count < r):
                part, ptr = getNodes(ptr, nodes+1)
                # print ptr.val
            else:
                part, ptr = getNodes(ptr, nodes)
            out.append(part)
            # print ptr.val
            count += 1

        return out

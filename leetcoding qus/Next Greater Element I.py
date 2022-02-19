# Qus:https://leetcode.com/problems/next-greater-element-i/

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        stack = []
        d = {}
        
        for num in nums2:
            if(stack==[]):
                stack.append(num)
            else:
                
                while(stack!=[] and stack[-1]<num):
                    d[stack.pop()] = num
                stack.append(num)
                
        ans = []
        for num in nums1:
            ans.append(d.get(num,-1))
        return ans
            
        
        
        
        
        
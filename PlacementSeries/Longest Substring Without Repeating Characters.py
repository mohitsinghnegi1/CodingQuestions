# Qus:https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d={}
        prev=0
        max1=0
        s=" "+s
        
        for i in range(1,len(s)):
            if(d.get(s[i]) and d.get(s[i])>prev):
                prev=d.get(s[i])
            d[s[i]]=i
            max1=max(i-prev,max1)
            
        return max1
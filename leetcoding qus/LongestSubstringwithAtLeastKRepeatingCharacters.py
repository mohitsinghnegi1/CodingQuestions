# Qus: https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/
def subproblem(s,k):
    if(s==""):
        # print "empyt"
        return 0
    #print s
    #find minimum frequency char based on count of each character 
    #it will return the char having minimum frequency
    #new syntax 
    c=min(set(s),key=s.count)
    
    if(s.count(c)>=k):
        return len(s)
    
    #since there are 26 lower char so it will move maximum for 26 debth
    #on each debth there is O(n) time complexity so total complexity would be nlong(n)
    
    #this function will create all possible substring created by excluding lowest frequency char if lowest frequency <k
    return max(subproblem(substring,k) for substring in s.split(c))
    


class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        #this function should return max length of substring
        #having frequency of each character >=k
        return subproblem(s,k)
                
            
               
                
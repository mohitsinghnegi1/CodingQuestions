# Qus:https://leetcode.com/problems/substring-with-concatenation-of-all-words/


"""
Intution: for every index check if the i+len(substring) contains all the words that is present is word list
time complexity O(N**2)

"""

from collections import Counter,defaultdict
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        
        count = Counter(words)
        # print count
        n = len(words)
        m = len(words[0])
        
        lenSub = n * m # length of substring
        ans = []
        
        # print counter2
        for i in range(0,len(s)-lenSub + 1):
        
            isSol = True
            
            counter2 = defaultdict(int)
        
            for j in range(i,i+lenSub,m):
                s1 = s[j:j+m]
                # print s,i,i+m
                counter2[s1] += 1
            
            for word in count:
                
                
                if(count[word]!=counter2[word]):
                    isSol=False
                    break
                
            if(isSol):
                ans.append(i)
        
        return ans
            
            
            
            
            
           
            
            
            
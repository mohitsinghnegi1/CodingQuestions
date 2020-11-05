# Qus:https://leetcode.com/problems/wildcard-matching/

# recursive solution in python 3
# TLE 1775 / 1811 test cases passed
@lru_cache
def regix(s,p,pos):
    
    if(s=='' and (pos==-1 or pos>=len(p))):
        return True 
    
    if(p=='' or s==''):
        return False
    if p[-1]=='*':
        return regix(s[:-1],p,pos) or regix(s,p[:-1],pos) 
    
    if p[-1]=='?' or p[-1]==s[-1]:
        return regix(s[:-1],p[:-1],pos)

    if(p[-1]!=s[-1]):
        return False
    

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
       
        # find the first pos of the char
        pos=-1
        for i in range(len(p)):
            if(p[i].isalpha() or p[i]=='?'):
                pos=i
                break
        # print(pos)
        return regix(s,p,pos)
    
    






        
        
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
    
    
# using dp O(n^2) 

    

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
       
        s=" "+s # we are adding extra space in front to consider the empty string also
        p=" "+p # we are adding extra space in front to consider the empty pattern also
        out=[]  # by default we setting val to false 
        for i in range(len(s)):
            v=[]
            for j in range(len(p)):
                v.append(0)
            out.append(v)
        
        out[0][0]=1 # empty string and empty pattern evalute to true
        
        # State 
        # out[i][j] represents if string upto index i is matched by pattern up to index j
        
        
        # print(p)
        # consider the empty string and a pattern of len i
        for i in range(1,len(p)):
            if(p[i]=='*'):
                out[0][i] =out[0][i-1] 
        
        
        for i in range(1,len(s)):
            for j in range(1,len(p)):
                # case when p[j]=='?' or p[j]==s[i] , if p(i-1,j-1) is matched then this                 # also matched 
                if(p[j]=='?' or p[j]==s[i]):
                    out[i][j]=out[i-1][j-1]
                
                # if p[j]=='*' then conside left and right , if any is true then cur will                 # match too
                elif(p[j]=='*'):
                    out[i][j]=out[i-1][j] or out[i][j-1] 
                
        # for i in out:
        #     print(i)
        return out[-1][-1]
        



        
        





        
        
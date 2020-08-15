# Qus:https://leetcode.com/problems/palindrome-partitioning/

def combinePart(prefix,subpart):
    #arrays that start with prefix
    # print "subpart",prefix,subpart
    out=[]
    for right in subpart:
        # print right
        v=[prefix]+right
        out.append(v)
        
    #return list of arrays whose first element is prefix
    return out
        

def givePartition(s):
    #if 
    if(s==''):
        return [[]]
    
    out=[]
    
    for i in range(len(s)):
        if(s[:i+1]==s[:i+1][::-1]):
            subpart=givePartition(s[i+1:])
            # print "subparts",subpart
            
            #this function will return all the valid ans which start with partition s[:i+1]
            a=combinePart(s[:i+1],subpart)
            
            #ans we add into out array
            out.extend(a)
            
    return out

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        #this functions will return list of all partitions possible
        #this problem can we divided into sub problemts
        
        return givePartition(s)
# https://leetcode.com/problems/longest-uncommon-subsequence-ii/

class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        
        def isSubseq(s1,s2):
            # print "s1,s2",s1,s2
            i = 0
            j = 0
            
            while(i<len(s1) and j<len(s2)):
                
                if(s1[i]==s2[j]):
                    i+=1
                j+=1
                # print "ij",i,j,len(s2)                
            # print i,"s1,s2",s1,s2,i==len(s1)
            return i==len(s1) # means all character are matched

        max1 = -1
        
        for i in range(len(strs)):
            flag = False
            for j in range(len(strs)):
                
                if(i!=j and isSubseq(strs[i],strs[j])):
                    flag = True
                    # print strs[i],strs[j]
                    break
            # print flag,strs[i]
            if(flag==False):  
                # print strs[i]
                max1 = max(len(strs[i]),max1)
        return max1
        
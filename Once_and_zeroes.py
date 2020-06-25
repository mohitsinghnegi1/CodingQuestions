
#Qus :https://leetcode.com/problems/ones-and-zeroes/submissions/

#sol 1 : take and not take with memorization ->tle 
def getCount(d,m,n,i=0):
    global dic
    if dic.get((m,n,i),None):
        return dic[(m,n,i)]

    if(i>=len(d) or m<0 or n<0):
        return 0
    #take current string only if it satisisfy below conditions
    take=0
    if(m-d[i][0]>=0 and n-d[i][1]>=0):
        take=1+getCount(d,m-d[i][0],n-d[i][1],i+1)
    
    #dont take current string
    dontTake=getCount(d,m,n,i+1)
    
    dic[(m,n,i)]=max(take,dontTake)
    return dic[(m,n,i)]
        
#create an array which will store count of 0 and 1
def getDictCount(strs):
    d=[]
    for i in range(len(strs)):
        zeros=strs[i].count('0')
        d.append([zeros,len(strs[i])-zeros])
    return d
        
    





class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        #this function will return dictionary in the form 
        #str:(number of 0,number of 1) in the string
        global dic
        dic={}
        d=getDictCount(strs)
        # print d
        return getCount(d,m,n)
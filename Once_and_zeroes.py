
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
        
    
#sol 2 using @functools.lru_cache(None) inpython 3 same method


class Solution:
    def findMaxForm(self, s: List[str], m: int, n: int) -> int:
        global strs
        global max1
        max1=0
        strs=s
        @functools.lru_cache(None)
        def solve(i,m,n):
            global max1

            if(i>=len(strs)):
                return 0
            zeros=strs[i].count('0')
            once=len(strs[i])-zeros

            notInc=solve(i+1,m,n)

            if (m-zeros)<0 or (n-once)<0:
                # print(i,m,n,notInc)
                return notInc
            #if after substraction we get positive value of m and n then we can include that str hence +1
            inc=1+solve(i+1,m-zeros,n-once)


            # print(i,m,n,max(inc,notInc))
            max1=max(max1,max(inc,notInc))
            return max(inc,notInc)
        
        solve(0,m,n)
        return max1
              
        
        




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
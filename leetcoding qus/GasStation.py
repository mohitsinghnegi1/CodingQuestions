# Qus:https://leetcode.com/problems/gas-station/
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
#         sol1

#         a=[i-j for i,j in zip(gas,cost)]
#         print a 
       
#         for i in range(len(a)):
            
#             k=(i+1)%len(a)
#             positive=a[i]
#             while(positive>=0):
#                 if(k==i):
#                     return i
                
#                 positive+=a[k]
#                 k=(k+1)%len(a)
#         return -1
        # sol2
        # Each element in the input arrays is a non-negative integer.
        
        if(sum(gas)<sum(cost)):
            return -1
        
        
        # why this logic works?
        # bec if you notice all number are non negative 
        # you will find that will sol exist if sum(gas)>=sum(cost)
        # if sum(gas)<sum(cost) then there exist no solution
        
        a=[i-j for i,j in zip(gas,cost)]
        
        balance=0
        pos=0
        for i in range(len(a)):
            balance+=a[i]
            
            if(balance<0):
                balance=0
                pos=i+1
        return pos
            
            
        
        
        
#User function Template for python3
# Qus:https://practice.geeksforgeeks.org/problems/possible-words-from-phone-digits-1587115620/1

class Solution:
    
    def __init__(self):
        self.map = {2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
    
    
    def solve(self,a,N,index,word,res):
       
       if(index==N):
           res.append(word)
           return
      
       for i in self.map[a[index]]:
           self.solve(a,N,index+1,word+i,res)
           

    #Function to find list of all words possible by pressing given numbers.
    def possibleWords(self,a,N,i=0):
        #Your code here
        if(i==N):
            return []
        
        
        
        res = []
        self.solve(a,N,0,'',res)
        return res
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math



def main():
    
    T=int(input())
    
    while(T>0):
        
        N=int(input())
        a=[int(x) for x in input().strip().split()]
        ob = Solution()
        res = ob.possibleWords(a,N)
        for i in range (len (res)):
            print (res[i], end = " ") 
        
        print()
       
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
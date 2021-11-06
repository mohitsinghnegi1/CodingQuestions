# Qus:https://practice.geeksforgeeks.org/problems/stickler-theif-1587115621/1
#User function Template for python3

class Solution:  
    
    #Function to find the maximum money the thief can get.
    def FindMaxSum(self,a, n):
        
        # code here
        
        dp = [0]*n
        
        
        for i in range(n):
            dp[i]=a[i]
            if(i-1>=0):
                dp[i] = max(dp[i-1],dp[i])
            if(i-2>=0):
                dp[i] = max(dp[i],dp[i-2]+a[i])
            if(i-3>=0):
                dp[i] =  max(dp[i],dp[i-3]+a[i])
            
        # print(dp)
        return dp[-1]
        
        
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
sys.setrecursionlimit(10**6)
# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.FindMaxSum(a,n))
# } Driver Code Ends
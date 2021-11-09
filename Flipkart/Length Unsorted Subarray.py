# Qus: https://practice.geeksforgeeks.org/problems/length-unsorted-subarray3022/1

#User function Template for python3
from bisect import bisect_left,bisect_right

class Solution:

	def printUnsorted(self,arr, n):
		# code here
		
		st = -1
		end = -1
		
		
		for i in range(1,n):
		    if(arr[i-1]>arr[i]):
		        st = i-1
		        break
		for i in range(n-2,-1,-1):
		    if(arr[i]>arr[i+1]):
		        end = i+1
		        break
		
		if(st==-1):
		    return [0,0]
# 		print(st,end)
		
		return [bisect_right(arr,min(arr[st:end+1]),0,st),bisect_left(arr,max(arr[st:end+1]),end+1,n)-1]
		
		
		   
		    
		        
		
		
		
		
		
		
		
		
		
		
		

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.printUnsorted(arr, n)
        print(str(ans[0]) + " " + str(ans[1]))
        tc -= 1

# } Driver Code Ends
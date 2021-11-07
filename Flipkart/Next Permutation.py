# Qus:https://practice.geeksforgeeks.org/problems/next-permutation5226/1

#User function Template for python3

class Solution:
    def nextPermutation(self, N, arr):
        # code here
        
        if(N<=1):
            return arr
    
        j = len(arr)-2
        while(j>=0 and arr[j]>=arr[j+1]):
            j-=1
        
        if(j==-1):
            return arr[::-1]
        
        justLarge = j+1
        for i in range(j+2,len(arr)):
            if(arr[j]<arr[i]<arr[justLarge]):
                justLarge = i
            
            if(arr[i]<arr[j]):
                break
        
        arr[j],arr[justLarge] = arr[justLarge],arr[j]
            
        # print(justLarge,j)
            
        
        return arr[:j+1]+arr[j+1:][::-1]
        # swap()
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        ans = ob.nextPermutation(N, arr)
        for i in range(N):
            print(ans[i],end=" ")
        print()
# } Driver Code Ends

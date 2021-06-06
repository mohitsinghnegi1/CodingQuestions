# Qus:https://practice.geeksforgeeks.org/problems/sieve-of-eratosthenes5242/1
# time compleixit O(nlog(log(n)))

# User function Template for python3

class Solution:
    def sieveOfEratosthenes(self, N):
    	# code here

    	n = 2

    	prime = [True]*(N+1)
    	prime[0] = False
    	prime[1] = False

    	i = 2
    	# break if next i*i value greater then N
    	while(i*i <= N):

    	    if(prime[i]):

        	    j = i*i  # just one step start next value from i*i for example 2*2 3*3
        	    while(j <= N):
        	        prime[j] = False
        	        j += i

        	i += 1
        	 
        
        out = []
        
        for i in range(2,N+1):
            if(prime[i]):
                out.append(i)
        
        return out
            

# { 
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.sieveOfEratosthenes(N)
        for i in ans:
            print(i, end=" ")
        print()
# } Driver Code Ends

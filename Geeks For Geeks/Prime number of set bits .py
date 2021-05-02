# Qus:https://practice.geeksforgeeks.org/problems/prime-number-of-set-bits4632/1

# User function Template for python3

def countSetBit(val):

    c = 0

    for i in range(12):
        if(val & 1 << i):
            c += 1
    return c


class Solution:
    def primeSetBits(self, L, R):
        # code here
    count = 0
    primes = set([2, 3, 5, 7, 11, ])
    for i in range(L, R+1):

        c = countSetBit(i)

        if(c in primes):
            count += 1

    return count


# {
#  Driver Code Starts
# Initial Template for Python 3
# Initial Template for Python 3
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        L, R = input().split()
        L = int(L)
        R = int(R)
        ob = Solution()
        print(ob.primeSetBits(L, R))

# } Driver Code Ends

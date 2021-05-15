# Qus:https://practice.geeksforgeeks.org/problems/wave-array-1587115621/1

# User function Template for python3


import math


class Solution:
    # Complete this function
    # Function to sort the array into a wave-like array.
    def convertToWave(self, A, N):
        # Your code here
        # this will work if and only if equal val can be adjecent
        for i in range(0, N, 2):

            if(i != 0 and A[i-1] > A[i]):
                A[i-1], A[i] = A[i], A[i-1]

            if(i != N-1 and A[i+1] > A[i]):
                A[i+1], A[i] = A[i], A[i+1]


# {
#  Driver Code Starts
# Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):

        N = int(input())

        A = [int(x) for x in input().split()]
        ob = Solution()
        ob.convertToWave(A, N)
        for i in A:
            print(i, end=" ")

        print()

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends

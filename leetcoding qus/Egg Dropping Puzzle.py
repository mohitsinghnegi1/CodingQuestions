# User function Template for python3
# Qus:https://practice.geeksforgeeks.org/problems/egg-dropping-puzzle-1587115620/1
import sys


class Solution:

    # Function to find minimum number of attempts needed in
    # order to find the critical floor.
    def eggDrop(self, n, f):
        # code here

        # 1. though : start from 0 and gradually increase the floor to drop the egg from : disadvange : lot of moves
        # 2. 

        # dp = {}

        # def minMoves(n,i,j):

        #     if(n==1):
        #         return j-i

        #     noFloors = j-i
        #     if(noFloors<=1):

        #         #print("j-i",j-i,j,i)
        #         return j-i

        #     if((n,i,j) in dp):
        #         return dp[(n,i,j)]

        #     min_moves = sys.maxsize

        #     for k in range(i, j):
        #         egg_break = 1 + minMoves(n-1,i,k)
        #         not_break = 1 + minMoves(n,k+1,j)

        #         min_moves = min(max(egg_break,not_break),min_moves)

        #     if(min_moves==sys.maxsize):
        #         #print(min_moves)
        #         min_moves =  0

        #     dp[(n,i,j)] =  min_moves
        #     return dp[(n,i,j)]

        # return minMoves(n,0,f)

        # dp = {}

        # def minMoves(n,floors):

        #     if(n==1):
        #         return floors

        #     if(floors==1 or floors==0):

        #         #print("j-i",j-i,j,i)
        #         return floors

        #     if((n,floors) in dp):
        #         return dp[(n,floors)]

        #     min_moves = sys.maxsize

        #     for k in range(1,floors+1):
        #         egg_break = 1 + minMoves(n-1,k-1)
        #         not_break = 1 + minMoves(n,floors-k)

        #         min_moves = min(max(egg_break,not_break),min_moves)

        #     if(min_moves==sys.maxsize):
        #         #print(min_moves)
        #         min_moves =  0

        #     dp[(n,floors)] =  min_moves
        #     return dp[(n,floors)]

        # return minMoves(n,f)

        dp = [[0] * (f + 1) for i in range(n + 1)]

        for floor in range(f + 1):
            dp[1][floor] = floor

        for egg in range(2, n + 1):
            dp[egg][0] = 0
            dp[egg][1] = 1

        for egg in range(2, n + 1):
            for floors in range(2, f + 1):
                min_moves = sys.maxsize

                for k in range(1, floors + 1):
                    egg_break = 1 + dp[egg - 1][k - 1]
                    not_break = 1 + dp[egg][floors - k]

                    min_moves = min(max(egg_break, not_break), min_moves)

                # if(min_moves==sys.maxsize):
                #     #print(min_moves)
                #     min_moves =  0

                dp[egg][floors] = min_moves

        return dp[n][f]


# {
# Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n, k = map(int, input().strip().split())
        ob = Solution()
        print(ob.eggDrop(n, k))
# } Driver Code Ends
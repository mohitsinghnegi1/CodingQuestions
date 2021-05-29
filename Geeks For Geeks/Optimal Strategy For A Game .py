# QUs:https://practice.geeksforgeeks.org/problems/optimal-strategy-for-a-game-1587115620/1
# Timecomplexity O(n**2) -- new approach
# User function Template for python3
import sys
import io
import atexit
from functools import lru_cache

# @lru_cache(maxsize = 100)


def findScores(i, j, d):

    if(i > j):
        return 0

    if(d.get((i, j), False) != False):
        return d.get((i, j))

    d[(i, j)] = max(arr[i] + min(findScores(i+2, j, d), findScores(i+1, j-1, d)),
                    arr[j] + min(findScores(i+1, j-1, d), findScores(i, j-2, d)))
    return d[(i, j)]


# Function to find the maximum possible amount of money we can win.
def optimalStrategyOfGame(arr, n):

    # code here
    if(n == 0):
        return 0

    d = {}

    return findScores(0, n-1, d)


# {
#  Driver Code Starts
# Initial Template for Python 3

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(optimalStrategyOfGame(arr, n))

# } Driver Code Ends

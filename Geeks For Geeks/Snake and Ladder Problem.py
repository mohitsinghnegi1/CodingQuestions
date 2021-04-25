# Qus:https://practice.geeksforgeeks.org/problems/snake-and-ladder-problem4816/1#

"""
Timecomplexity : O(n*6) which is 30 

"""


# User function Template for Python3
from collections import deque


def minMoves(moves, end):
    # print(moves)
    queue = deque([])
    visited = {}

    # cell , distance, Note we are initially at first cell
    queue.append((1, 0))

    while(queue):
        v, d = queue.popleft()
        if(v == end):
            return d
        visited[v] = True

        for i in range(v+1, min(v+7, end+1)):

            if(i not in visited):
                if(moves[i] != -1):
                    queue.append((moves[i], d+1))
                else:
                    queue.append((i, d+1))

    return -1


class Solution:
    def minThrow(self, N, arr):
        totalCells = 5*6

        moves = [-1]*(totalCells+1)

        for i in range(0, 2*N, 2):
            moves[arr[i]] = arr[i+1]

        # now we have moves in place

        return minMoves(moves, totalCells)


# {
#  Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(2*N):
            arr[i] = int(arr[i])

        ob = Solution()
        print(ob.minThrow(N, arr))
# } Driver Code Ends


# little faster then privisous*************************************
# User function Template for Python3


def minMoves(moves, end):
    # print(moves)
    queue = deque([])
    visited = {}

    # cell , distance, Note we are initially at first cell
    queue.append((1, 0))

    while(queue):
        v, d = queue.popleft()
        if(v == end):
            return d
        visited[v] = True

        for i in range(v+1, min(v+7, end+1)):

            if(i not in visited):
                if(moves[i] != -1):
                    queue.append((moves[i], d+1))
                else:
                    queue.append((i, d+1))

    return -1


class Solution:
    def minThrow(self, N, arr):
        totalCells = 5*6

        moves = [-1]*(totalCells+1)

        for i in range(0, 2*N, 2):
            moves[arr[i]] = arr[i+1]

        # now we have moves in place

        return minMoves(moves, totalCells)


# {
#  Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(2*N):
            arr[i] = int(arr[i])

        ob = Solution()
        print(ob.minThrow(N, arr))
# } Driver Code Ends

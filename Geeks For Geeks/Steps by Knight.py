
# Qus:https://practice.geeksforgeeks.org/problems/steps-by-knight5927/1#
"""
Timecomplexity O(n**2)
"""
from collections import deque


def isInside(x, y, N):

    if (x >= 1 and x <= N and y >= 1 and y <= N):
        return True
    return False


class Solution:
    def minStepToReachTarget(self, knightpos, targetpos, N):
        # Code here

        if(knightpos == targetpos):
            return 0

        dx = [2, 2, -2, -2, 1, 1, -1, -1]
    dy = [1, -1, 1, -1, 2, -2, 2, -2]

    queue = deque()

    # push starting position of knight
    # with 0 distance
    queue.append((knightpos, 0))

    # make all cell unvisited
    visited = [[False for _ in range(N+1)] for _ in range(N+1)]

    # visit starting state
    visited[knightpos[0]][knightpos[1]] = True

    while(queue):
        [x, y], dist = queue.popleft()
        if[x, y] == targetpos:
            return dist

        for i in range(8):

            if(isInside(x+dx[i], y+dy[i], N)):

                if visited[x+dx[i]][y+dy[i]] == False:
                    queue.append(([x+dx[i], y+dy[i]], dist+1))
                    visited[x+dx[i]][y+dy[i]] = True

    return -1


# {
#  Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N = int(input())
        KnightPos = list(map(int, input().split()))
        TargetPos = list(map(int, input().split()))
        obj = Solution()
        ans = obj.minStepToReachTarget(KnightPos, TargetPos, N)
        print(ans)

# } Driver Code Ends

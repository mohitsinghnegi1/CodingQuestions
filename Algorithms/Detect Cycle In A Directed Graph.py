# Qus: https://www.codingninjas.com/studio/problems/1062626?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&leftPanelTab=0
from collections import deque


def detectCycleInDirectedGraph(n, edges):
    # Write your code here
    visited = [False] * (n + 1)
    recStack = [False] * (n + 1)

    adj = [[] for i in range(n + 1)]

    for u, v in edges:
        adj[u].append(v)

    def dfs(src):
        visited[src] = True
        recStack[src] = True

        for v in adj[src]:
            if (visited[v] == False):
                if (dfs(v)):
                    return True
            elif (recStack[v] == True):
                return True

        recStack[src] = False
        return False

    for u in range(1, n + 1):
        if (visited[u] == False):
            if (dfs(u)):
                return True

    return False
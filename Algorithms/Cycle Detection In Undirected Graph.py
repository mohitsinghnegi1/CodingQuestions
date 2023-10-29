#Qus:https://www.codingninjas.com/studio/problems/1062670?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&leftPanelTab=0

from collections import deque


def cycleDetection(edges, n, m):
    # Write your code here.
    # Return "Yes" if cycle id present in the graph else return "No".

    visited = set()

    adj = [[] for i in range(n + 1)]

    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    def bfs(src):
        queue = deque()
        queue.append((src, -1))
        visited.add(src)

        while (queue):
            u, par = queue.popleft()

            for v in adj[u]:

                if (v != par and v in visited):
                    return True

                if (v != par):
                    queue.append((v, u))
                    visited.add(v)

        return False

    for u in range(1, n + 1):
        if (u not in visited):
            if (bfs(u)):
                return "Yes"

    return "No"


# using bfs

from collections import deque


def cycleDetection(edges, n, m):
    # Write your code here.
    # Return "Yes" if cycle id present in the graph else return "No".

    visited = set()

    adj = [[] for i in range(n + 1)]

    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    def dfs(src):
        queue = deque()
        queue.append((src, -1))
        visited.add(src)

        while (queue):
            u, par = queue.pop()

            for v in adj[u]:

                if (v != par and v in visited):
                    return True

                if (v != par):
                    queue.append((v, u))
                    visited.add(v)

        return False

    for u in range(1, n + 1):
        if (u not in visited):
            if (dfs(u)):
                return "Yes"

    return "No"
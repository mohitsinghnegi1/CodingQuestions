# Qus : https://practice.geeksforgeeks.org/problems/topological-sort/1#
# video : https://www.youtube.com/watch?v=Yh6EFazXipA     u - > v   u comes first in toplogical sort  this recursion is possible for DAG
# time complexity is O(v+E)
'''
    Implement Topological sort using recursion

    Note :
    It is valid even for multiple disconnected components
    It is not valid if there is any cycle 
    The graph should be Directed and Acyclic (DAG)

'''

import sys
from collections import defaultdict
# Your task is to complete this function
# Function should return Topologically Sorted List
# Graph(adj) is a defaultict of type List
# n is no of edges

# this method is not valid if this graph may contains cycles


def topoSort(n, adj):
    # Code here
    # return arr
    # creating generic topological sorting
    # arr could be of any type
    arr = range(0, n)
    stack = []  # we need to return reverse of stack
    # visited can contain any data type also
    visited = set()

    # this topological sort function will sort one connected component
    # this code will not able to detect a cycle
    # so to detect cycle we can use indegree method or
    # we can maintain a 3 state unprocessed -0 processing -1 processed-2
    # https://codeforces.com/blog/entry/4907

    # In this function we  first append child in stack then root
    # if we already visited the child node then we will not process it again

    def topologicalSort(val):
        visited.add(val)
        for child in adj[val]:
            if(child not in visited):
                topologicalSort(child)
                stack.append(child)

    # to handle topological sorting for multiple disconnected component
    # we are using a visited set
    # we are using stack to store the ans in reverse order
    for val in arr:
        if(val not in visited):
            topologicalSort(val)
            stack.append(val)

    # reverse the stack
    return(stack[::-1])


'''
Input:
6 6
5 0
5 2
2 3
4 0
4 1
1 3

'''


e, n = map(int, raw_input().split())
graph = defaultdict(list)

# not required
# for i in range(n):
#     graph[i]=[]

# create a graph
for i in range(e):
    u, v = map(int, raw_input().split())
    graph[u].append(v)

# return stack in reverse order
out = topoSort(n, graph)
print(out)


# iterative way using stack and indegree with kye as  node value as count , outegree u-> [v1,v2]


class Solution:

    # Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here

        # indegree means , i am dependent on other
        # v is dependent on u

        indegree = {}
        # O(n)
        for i in range(len(adj)):
            indegree[i] = 0
        # outdegree = defaultdict(set)

        for u in range(len(adj)):
            for v in adj[u]:
                indegree[v] += 1
                # outdegree[u].add(v)

        # now we have indegree map , it will tell how many nodes the ky is dependent on

        # first process all the 0 degree
        topo = []
        stack = []

        def addZeroIndegree():
            for v in indegree:
                if(indegree[v] == 0):
                    stack.append(v)

        addZeroIndegree()

        while(stack):
            u = stack.pop()
            topo.append(u)

            # now i have remove a node whose indegree was 0
            # we can check if all node nodes he is pointing to -1 will make their
            # indegree 0

            for v in adj[u]:
                indegree[v] -= 1
                if(indegree[v] == 0):
                    stack.append(v)

        if len(adj) != len(topo):
            return -1

        return topo


# {
#  Driver Code Starts
# Driver Program
sys.setrecursionlimit(10**6)


def check(graph, N, res):
    map = [0]*N
    for i in range(N):
        map[res[i]] = i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        e, N = list(map(int, input().strip().split()))
        adj = [[] for i in range(N)]

        for i in range(e):
            u, v = map(int, input().split())
            adj[u].append(v)

        ob = Solution()

        res = ob.topoSort(N, adj)

        if check(adj, N, res):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends


# revision using recursion


# question to ask from interviewer if this graph is acyclic or not , if not
# what should i print then
class Solution:

    # Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here

        visited = {}
        stack = []  # push the child then the parent always

        def dfs(v):

            visited[v] = True  # we have viisted this child first

            # let suppose it is the par of someone then there will be adj child
            for nei in adj[v]:
                if(nei not in visited):
                    dfs(nei)  # this will make sure that put the child first in stack

            # put it back into stack (ie if no one is dependent on it
            # then just it will be only child that is dependent on other)
            stack.append(v)

        for v in range(len(adj)):

            if(v not in visited):
                dfs(v)
        stack.reverse()
        return stack
# {
#  Driver Code Starts
# Driver Program


sys.setrecursionlimit(10**6)


def check(graph, N, res):
    map = [0]*N
    for i in range(N):
        map[res[i]] = i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        e, N = list(map(int, input().strip().split()))
        adj = [[] for i in range(N)]

        for i in range(e):
            u, v = map(int, input().split())
            adj[u].append(v)

        ob = Solution()

        res = ob.topoSort(N, adj)

        if check(adj, N, res):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends

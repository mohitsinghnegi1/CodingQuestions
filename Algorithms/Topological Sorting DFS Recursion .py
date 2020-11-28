# Qus : https://practice.geeksforgeeks.org/problems/topological-sort/1#

'''
    Implement Topological sort using recursion

    Note :
    It is valid even for multiple disconnected components
    It is not valid if there is any cycle 
    The graph should be Directed and Acyclic (DAG)

'''

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

    # In this function we are first append child in stack then root
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

'''
# Sample code to perform I/O:

name = raw_input()          # Reading input from STDIN
print 'Hi, %s.' % name      # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

'''
    Time complexity 
    O(N+E)
    Space complexity 
    O(N)
'''


# Write your code here
n, m = map(int, raw_input().split())

indegree = {}
graph = {}

# dont use default dict here
for i in range(1, n+1):
    indegree[i] = 0
    graph[i] = []

for i in range(m):
    u, v = map(int, raw_input().split())
    indegree[v] += 1
    graph[u].append(v)

# now we have indegree of all nodes
# we have parent -> childs map also

# time complexity of this approach is O(nlogn) since i have visited all nodes and to heapify
# we require logn time


def pushElementWithIndegreeZeroInto(stack):
    for i in indegree:
        if(indegree[i] == 0):
            stack.append(i)


# print indegree
# print graph
# first push all the eleement whose indegree is 0 into stack
stack = []  # using heap bec it maintain all the elements in lexigraphical order
pushElementWithIndegreeZeroInto(stack)

topological_seq = []

while(stack):
    # pop the elemement from heap
    node = stack.pop()
    topological_seq.append(node)
    # reduce the degree of all its child node , also check if the new indegree of
    # child nodes is =0 then push it into heap again
    for child in graph[node]:
        indegree[child] -= 1
        if(indegree[child] == 0):
            stack.append(child)
    # delete this node
    # delete the processed node
    del indegree[node]
    del graph[node]

# print topological_seq
if(len(topological_seq) != n):
    print -1

print " ".join(map(str, topological_seq))



# Easy to understand using BFS/DFS only


class Solution:

    # Function to return list containing vertices in Topological order.
    def topoSort(self, n, adj):
        # Code here

        indegree = {}

        for i in range(n):
            indegree[i] = 0

        for u in range(n):
            for v in adj[u]:
                indegree[v] += 1

        queue = []

        for u in range(n):
            if (indegree[u] == 0):
                queue.append(u)

        topo = []

        while (queue):

            u = queue.pop()

            topo.append(u)

            for v in adj[u]:
                indegree[v] -= 1
                if (indegree[v] == 0):
                    queue.append(v)

        return topo


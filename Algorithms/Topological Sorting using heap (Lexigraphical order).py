# Qus: https://www.hackerearth.com/practice/algorithms/graphs/topological-sort/tutorial/
'''
    Intution :
    Remember : u->v   means v is dependent on u , which means we need to process u before v
    How to create a indegree graph 
    How to create a graph for storing parent child relationship
    we need to increament indegree[v]+=1 to calculate the indegree graph since u is pointing to v
    we need to push graph[u].append(v) because we need to know who are the child of this node , 
    so that we can reduce the indegree of those node , after pushing cur node and deleting it from the graph
    
    Pick the nodes having indegree 0
    and push all these nodes into heap (according to ques we need lexigraphical ordering)

    so loop while heap is not empty 
    -   pop min val element from the heap having indegree 0
    -   triverse trough its child node and reduce indegree of those child
    -   if the indegree of child is zero then push into the heap
    -   one all child are processed delete the poped node from the indegree and graph

    Data Structures Used:
    -   heap     (to get min val element with indegree zero)
    -   graph    (indegree , graph)
'''

'''
# Sample code to perform I/O:

name = raw_input()          # Reading input from STDIN
print 'Hi, %s.' % name      # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
from heapq import heappush, heappop, heapify
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


def pushElementWithIndegreeZeroInto(heap):
    for i in indegree:
        if(indegree[i] == 0):
            heappush(heap, i)


# print indegree
# print graph
# first push all the eleement whose indegree is 0 into stack
heap = []  # using heap bec it maintain all the elements in lexigraphical order
pushElementWithIndegreeZeroInto(heap)

topological_seq = []

while(heap):
    # pop the elemement from heap
    node = heappop(heap)
    topological_seq.append(node)
    # reduce the degree of all its child node , also check if the new indegree of
    # child nodes is =0 then push it into heap again
    for child in graph[node]:
        indegree[child] -= 1
        if(indegree[child] == 0):
            heappush(heap, child)
    # delete this node
    # delete the processed node
    del indegree[node]
    del graph[node]

# print topological_seq
if(len(topological_seq) != n):
    print -1

print " ".join(map(str, topological_seq))

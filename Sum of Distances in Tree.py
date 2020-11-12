# Qus:https://leetcode.com/problems/sum-of-distances-in-tree/

def getDistMatrixTemplate(N):
    # construct dist matrix
    dist=[]
    #dist[u][v] = distance between u and v 
    for _ in range(N):
        v=[]
        for _ in range(N):
            v.append(-1)
        dist.append(v)
    return dist

def constructTree(N,edges):
    tree={}
    for i in range(N):
        tree[i]=[]
    for u,v in edges:
        tree[u].append(v)
        tree[v].append(u)
   
    return tree
    
def dfs(source,tree,dist):
    
    stack=[[source,0]]
    v=set([source])
    
    while(stack):
        dest,level=stack.pop()
        dist[source][dest]=level
        
        for nxtChild in tree[dest]:
            if(nxtChild not in v):
                stack.append([nxtChild,level+1])
                v.add(nxtChild)
    return
    
def constructDistMatrix(dist,tree):
    #{0: [1, 2], 1: [0], 2: [0, 3, 4, 5], 3: [2], 4: [2], 5: [2]}
    N=len(tree.keys())
    
    for source in range(N):
        dfs(source,tree,dist)
    return dist

def constructArrayOfSumOfDistancesWithOtherNodes(tree,dist):
    sumArr=[]
    for src in range(len(dist)):
        distSrcDest=0
        for dest in range(len(dist)):
            distSrcDest+=dist[src][dest]
        sumArr.append(distSrcDest)
    return sumArr
                

class Solution(object):
    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        
        tree=constructTree(N,edges)
        
        dist=getDistMatrixTemplate(N)
       
        constructDistMatrix(dist,tree)
        
        # now we know the distance between any two nodes
        # now we need to construct array of int , representing sum of distances 
        # from current node to any other nodes in the given tree
        
        sumArr=constructArrayOfSumOfDistancesWithOtherNodes(tree,dist)
        
        return sumArr
        
        
        
        
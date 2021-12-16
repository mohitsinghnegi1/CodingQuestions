# Qus:https://leetcode.com/problems/minimum-height-trees/

# time complexity O(n)

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        
        if(n==1):
            return [0]
        
        indegree = {}
        graph = {}
        
        for i in range(n):
            indegree[i] = 0
            graph[i]=[]
        
        for u,v in edges:
            
            indegree[u]+=1
            indegree[v]+=1
            graph[u].append(v)
            graph[v].append(u)
            
        
        stack = []
        
        for i in range(n):
            if(indegree[i]<=1):
                stack.append(i)
    
        ans = []
        
        
        while(n>2):
            
            inner = []

            n -= len(stack)
            
            while(stack!=[]):
                node  = stack.pop()
                
                for nei in graph[node]:
                    
                    indegree[nei]-=1
                    
                    if(indegree[nei]==1):
                        inner.append(nei)
            stack = inner
        
  
        return stack
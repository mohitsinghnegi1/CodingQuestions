from collections import defaultdict

class Graph(object):
    
    def __init__(self,graph=defaultdict(list),directed=False,weighted=False):
        self.graph=graph
        self.directed=directed
        self.weighted=weighted
        
    def addEdge(self,u,v):
        
        self.graph[u].append(v)
        if(not self.directed):
            self.graph[v].append(u)
    
    def printGraph(self):
        
        for i in self.graph:
            print i," => ",self.graph[i]
            
            
    def dfs(self,root):
        
        print 'DFS'

        stack=[]
        visited=[root]
        stack.append(root)
        while(stack):
            node=stack.pop()
            print node,
            for i in self.graph[node]:
                if(i not in visited):
                    stack.append(i)
                    visited.append(i)
            
        
    
    def bfs(self,root):
        print 'BFS'
        queue=[]
        visited=[root]
        queue.append(root)
        while queue:
            node=queue.pop(0)
            print node,
            for i in self.graph[node]:
                if(i not in visited):
                    queue.append(i)
                    visited.append(i)
            
            
obj=Graph()
obj.addEdge('1','2')
obj.addEdge('2','3')
obj.addEdge('3','4') 
obj.addEdge('2','4')
obj.printGraph()   
obj.dfs('1')
obj.bfs('1')    
    

        
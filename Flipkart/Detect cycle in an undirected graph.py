# Qus:https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1

# using dfs
class Solution:
    
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V, adj):
	    
		#Code here
		
		
		# if there is a self loop then return true
# 		print(adj)
		
		
		visited = [False]*V
		
		def subgraphCosntainsLoop(i,par):
		    
		    
		    
		    visited[i] = True
		    
		    for nei in adj[i]:
		        
		        if(visited[nei]==False):
		            if(subgraphCosntainsLoop(nei,i)):
		                
		                return True
		        else:
		            
		            if(nei != par):
		                
		                return True
		      
		    return False      
		  

		ans = False
		for i in range(V):
		    if(visited[i]==False):
		        if(subgraphCosntainsLoop(i,-1)):
		            return True
		return ans
		
		
		
		
		
		
		
		
		

#{ 
#  Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends
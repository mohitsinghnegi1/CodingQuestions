# Qus:https://www.codingninjas.com/codestudio/problems/time-to-burn-tree_630563?source=youtube&amp;campaign=Striver_Tree_Videos&amp;utm_source=youtube&amp;utm_medium=affiliate&amp;utm_campaign=Striver_Tree_Videos&leftPanelTab=0

# intution: use parent pointer and do recursion or bfs to find time

from sys import stdin,setrecursionlimit
from queue import Queue

setrecursionlimit(10**7)

# Binary tree node class for reference.
class BinaryTreeNode :

	def __init__(self, data) :
		self.data = data
		self.left = None
		self.right = None
    
        

def setParent(node,par,parDict):
    
    if(node==None):
        return 
    
    parDict[node] = par
    setParent(node.left,node,parDict)
    setParent(node.right,node,parDict)
    
def burnTree(node,visited,parDict):
    
    if(node==None or node in visited):
        return 0
    
    visited[node] = True
   
    
    time = 1 + max(burnTree(node.left,visited,parDict),burnTree(node.right,visited,parDict),burnTree(parDict.get(node,None),visited,parDict))
    
    return time
    
    
    
    
    
    
    

def timeToBurnTree(root, start):

    # Write your code here.
    if(root==None):
        return 0
    parDict = {}
    setParent(root,None,parDict)
    visited = {}

    startNode = None
    for node in parDict:
        
        if(node.data==start):
            startNode = node
       
            break
    
    return burnTree(startNode,visited,parDict)-1
    
    
    
    











# Fast input
def takeInput() :
	
    arr = list(map(int, stdin.readline().strip().split(" ")))

    rootData = arr[0]

    n = len(arr)

    if(rootData == -1) :
        start = int(input().strip())
        return None, start

    root = BinaryTreeNode(rootData)
    q = Queue()
    q.put(root)
    index = 1
    while(q.qsize() > 0) :
        currentNode = q.get()  
        
        leftChild = arr[index]
        
        if(leftChild != -1) :
            leftNode =  BinaryTreeNode(leftChild)  
            currentNode.left = leftNode  
            q.put(leftNode)  
        
        index += 1
        rightChild = arr[index]
        
        if(rightChild != -1) :
            rightNode = BinaryTreeNode(rightChild)
            currentNode .right = rightNode  
            q.put(rightNode)  

        index += 1

    start = int(input().strip())

    return root, start

#main

root, start = takeInput()

print(timeToBurnTree(root, start))
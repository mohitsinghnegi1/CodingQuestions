# Qus:https://leetcode.com/problems/word-search/



class Solution(object):
    def __init__(self):
        self.ans=False
        
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        n=len(board)#row
        m=len(board[0])#col
        
        #we are passing coordinate to dfs function 
        #we are also passing level to avoid any space complexity
        def bfs(i,j,level=0):
            
            #if we are at level which is eqal to len of word then it means
            #all previous char are present in sequential order
            if(level==len(word)):
                self.ans=True
                return 
            #these are the condition fo which we need to return 
            if(i<0 or i>=n or j<0 or j>=m or word[level]!=board[i][j] or board[i][j]=='#' or self.ans):
                return 
            
            board[i][j]='#'
            #for all bfs below this will have board[i][j]='#'
            bfs(i-1,j,level+1)
            bfs(i+1,j,level+1)
            bfs(i,j-1,level+1)
            bfs(i,j+1,level+1)
            
            #once all the path are process we need to undo the change in board array
            #backtrack
            board[i][j]=word[level]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if(self.ans):
                    break
                #start bfs from the cell whose char is equal to first char of the word
                if(word[0]==board[i][j]):
                    bfs(i,j)
                
    
        return self.ans
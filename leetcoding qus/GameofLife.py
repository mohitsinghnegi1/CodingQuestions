# Qus: https://leetcode.com/problems/game-of-life/





class Solution(object):
    
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        #see the solution section for 3 best approches 😊 
        
        def applyRule(board,i,j):
            
            n=len(board)
            m=len(board[0])
            live=0
           
            #trick for comparing 8 cordintes
            x=[1,0,-1,0,-1,1,-1,1]
            y=[1,1,1,-1,-1,-1,0,0]
            
            #logic to count number of live cells in all 8 direction
            for k in range(8):
            
                if(i+x[k]>=0 and i+x[k]<n and j+y[k]>=0 and j+y[k]<m  ):
                    if(abs(board[i+x[k]][j+y[k]])==1):
                        live+=1

            #this is the logic to make algorithm inplace
            #all four rules applied
            if(live<2 or live>=4):
                if(board[i][j]==1):
                    board[i][j]=-1
            elif(live==3):
                if(board[i][j]==0):
                    board[i][j]=2
            

        for i in range(len(board)):
            for j in range(len(board[0])):
                
                applyRule(board,i,j)
        #print board
        
        #logic to make all dead cell as 0 and all live cell as 1
        for i in range(len(board)):
            for j in range(len(board[0])):
                
                if(board[i][j]==-1):
                    board[i][j]=0
                elif(board[i][j]==2):
                    board[i][j]=1
        
        return board
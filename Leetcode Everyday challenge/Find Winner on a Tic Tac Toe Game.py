# Qus:https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/

def check(ttt):
    # col
    if(ttt[0][0]==ttt[1][0]==ttt[2][0]!=0):
        return True
    if(ttt[0][1]==ttt[1][1]==ttt[2][1]!=0):
        return True
    if(ttt[0][2]==ttt[1][2]==ttt[2][2]!=0):
        return True
    # row
    if(ttt[0][0]==ttt[0][1]==ttt[0][2]!=0):
        return True
    if(ttt[1][0]==ttt[1][1]==ttt[1][2]!=0):
        return True
    if(ttt[2][0]==ttt[2][1]==ttt[2][2]!=0):
        return True
    if(ttt[0][0]==ttt[1][1]==ttt[2][2]!=0):
        return True
    if(ttt[0][2]==ttt[1][1]==ttt[2][0]!=0):
        return True
    
    return False




class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        ttt = [[0]*3 for i in range(3)]
    
        count = 0
        for x,y in moves:
            
            if(count%2==0):
                ttt[x][y]= -1
            else:
                ttt[x][y] = 1
            for i in range(3):
                print ttt[i]
            print "______"
            if(count>=2 and check(ttt)==True):
                if(count%2==0):
                    return 'A'
                else:
                    return 'B'
            count += 1
                
        
        if(count<=8):
            return "Pending"
                
        return "Draw"
            
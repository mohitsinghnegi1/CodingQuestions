Qus:https://leetcode.com/problems/predict-the-winner/

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:

        """
        :type nums: List[int]
        :rtype: bool
        """        
        @lru_cache(None)
        def getScore(start,end,turn):
    
            #base case when there is one element only
            #turn =1 denotes 1st player 
            #turn =0 denaotes 2nd player


            if(start==end and turn==1):
                return nums[start]
            elif(start==end and turn==0):
                return -nums[start]

            #will follow top to bottom approach

            left_res=getScore(start+1,end,(turn+1)%2)
            right_res=getScore(start,end-1,(turn+1)%2)


            if turn==1:

                #return res to its parent
                #if player 1 turn then we need to add so that at the end if res positive 
                #then we need to return True else false
                return max(left_res+nums[start],right_res+nums[end])
            else:

                #if player 2 turn then we need to substract
                return min(left_res-nums[start],right_res-nums[end])



        
        #1)what should be the arguments
        #2)start,end  will denaote begining,end index of the array respectively
        #3)turn will denaote whose turn is this
        #4)res will be negative if score of player 2 is more and 0 if equal and >0 if
        #player 1 score is more then player2
        #5)this is game theroy question using minmax algorithm
        
        
        res=getScore(0,len(nums)-1,1)
        
        
        return res>=0
        
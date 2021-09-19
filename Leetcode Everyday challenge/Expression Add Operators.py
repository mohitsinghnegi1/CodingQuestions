# Qus:https://leetcode.com/problems/expression-add-operators/solution/
# time complexity O(N*4^N)
# Reference : https://www.youtube.com/watch?v=uhZeoivB7_4
def solve(num,i,target,ans,st,d):
    
    if(i>=len(num)):
        # print st
        
        evaluated = d.get(st,eval(st))
        d[st] = evaluated
        
        if(target-evaluated==0):
            ans.append(st)
        return
    
    
    for j in range(i,len(num)):
        cur = st+num[i:j+1]
        # print "cur",cur,st,i
        
        if(j==len(num)-1):
            solve(num,j+1,target,ans,cur,d)
        else:
            for k in ['+','-','*']:
                stn = cur+k
                solve(num,j+1,target,ans,stn,d)
        if(num[i]=='0' ):
            return


class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        ans = []
        d = {}
        solve(num,0,target,ans,'',d)
        return ans


# efficient solution
# 4^(N-1) time complexity

class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """

        def solve(target,prev,total,st,i):
    
            if(i>=len(num)):
                # print st

                if(target-total==0):
                    ans.append(st[1:])
                return
            sign = st[-1]

            
            for j in range(i,len(num)):

                num2 = num[i:j+1] # koi number hai after sign
                # print "cur",cur,st,i
                
                if(j==len(num)-1):
                    # handle case where j is last we dont need to add 
                    if(sign=='+'):
                        solve(target,int(num2),total+int(num2),st+num2,j+1)
                    if(sign=='-'):
                        solve(target,-int(num2),total-int(num2),st+num2,j+1)
                    if(sign=='*'):
                        solve(target,prev*int(num2),total-prev + prev*int(num2),st+num2,j+1)
                    
                    return
                
                # print num2
                if(sign=='+'):
                    solve(target,int(num2),total+int(num2),st+num2+'+',j+1)
                    solve(target,int(num2),total+int(num2),st+num2+'-',j+1)
                    solve(target,int(num2),total+int(num2),st+num2+'*',j+1)
                elif(sign=='-'):
                    solve(target,-int(num2),total-int(num2),st+num2+'+',j+1)
                    solve(target,-int(num2),total-int(num2),st+num2+'-',j+1)
                    solve(target,-int(num2),total-int(num2),st+num2+'*',j+1)
                elif(sign=='*'):
                    
                    
                    solve(target,prev*int(num2),total-prev + prev*int(num2),st+num2+'+',j+1)
                    solve(target,prev*int(num2),total-prev + prev*int(num2),st+num2+'-',j+1)
                    solve(target,prev*int(num2),total-prev + prev*int(num2),st+num2+'*',j+1)
                if(num[i]=='0' ):
                    return
        
        ans = []
        prev = 0 
        total = 0
        
        
        solve(target,prev,total,'+',0)
        return ans

# cleaner solution
class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """

        def solve(target,prev,total,st,i):
    
            if(i>=len(num)):
                # print st

                if(target-total==0):
                    ans.append(st)
                return
            
            for j in range(i,len(num)):
                num2 = num[i:j+1] # koi number hai after sign
                # print "cur",cur,st,i
                
                if(i==0):
                    solve(target,int(num2),int(num2),num2,j+1)
                else:
                
                    solve(target,int(num2),total+int(num2),st+"+"+num2,j+1)
                    solve(target,-int(num2),total-int(num2),st+"-"+num2,j+1)
                    solve(target,prev*int(num2),total-prev+prev*int(num2),st+'*'+num2,j+1)
               
                if(num[i]=='0' ):
                    return
        
        ans = []
        prev = 0 
        total = 0
        
        
        solve(target,prev,total,'',0)
        return ans
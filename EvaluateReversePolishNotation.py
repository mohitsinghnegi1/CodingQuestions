# Qus :https://leetcode.com/problems/evaluate-reverse-polish-notation/

def evaluate(a,b,operator):
    a=int(a)
    b=int(b)

    if(operator=='+'):
        return str(b+a)
    if(operator=='-'):
        return str(b-a)
    if(operator=='*'):
        return str(b*a)

    if(operator=='/'):
        return str(floor(b/a)) if b/a>=0 else str(ceil(b/a))

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        # evaluate reverse polish notation
        # 1) insert number into stack 
        # 2) if we encounter operator then pop top two elemnt from the stack ie a,b  
        # 3) evalute b operator a and push result into stack
        # 4) the result will be the last remaining element in the stack
        # Note : in python if b/a >0 then return floor value else return ceil value
        

        op='+-*/'
        # print -133/132
        stack=[]
        i=0
        while(i<len(tokens)):
            if(tokens[i] not in op):
                stack.append(tokens[i])
            else:
                a=stack.pop()
                b=stack.pop()
                res=evaluate(a,b,tokens[i])
                
                stack.append(res)
            # print stack
            
            i+=1
        return stack[0]
        






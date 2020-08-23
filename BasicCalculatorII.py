# Qus :https://leetcode.com/problems/basic-calculator-ii/
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        #this function will return next int
        def getNext(s,i):
            
            i=i+1
            
            num2=0
            while(i<len(s) and s[i].isdigit()):
                num2=num2*10+int(s[i])
                i+=1
            return (num2,i-1)
            
        
        #this will contain positive or neg numbers based onn + and - sign
        stack=[]        
        i=0
        
        #this is to remove all spaces in string
        s=s.split(' ')
        s="".join(s)
        
        #stack will contain int not string
        
        while(i<len(s)):
            
            if(s[i].isdigit()):
                #if int then check top elemnt at stack if also number then combine it and push again
                if(stack==[] or not str(stack[-1]).isdigit()):
                    stack.append(int(s[i]))
                else:
                    if(str(stack[-1]).isdigit()):
                        stack.append(stack.pop()*10+int(s[i]))
                        
                
            else:
                #if current elemnt is operator then in case of + and - push to stack 
                #in case of *and / then apply operation and push ans to stack
                if(s[i]=="+" or s[i]=='-'):
                    stack.append(s[i])
                else:
                    op=s[i]
                    num1=stack.pop()
                    num2,i=getNext(s,i)
                    # print "=>",num1,num2,s[i]
                    if(op=='*'):
                        num3=num1*num2
                    else:
                        num3=num1/num2
                    stack.append(num3)
                
            
            i+=1
        # print stack
        
        sum1=0
        op="+"
        #at the end stack contains only + and - and number 
        #calculate result
        for i in range(len(stack)):
            if(stack[i]=='-'):
                op='-'
            elif(stack[i]=='+'):
                op='+'
            else:
                if(op=='+'):
                    sum1+=stack[i]
                else:
                    sum1-=stack[i]
            
        return sum1
        
#efficient approach

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s="".join(s.split(" "))
        now=''
        op='+'
        stack=[]
        #mark end since every time operator comes it evalute prev and now with the previous operator
        s+='#'
        
        for i in range(len(s)):
            #calculate the number
            if(s[i].isdigit()):
                now+=s[i]
                continue
            
            #in case prev op == - or + push "now" into stack
            #else calculate prev * now or prev/now
            #handle negative number division
            
            if(op=='+'):
                stack.append(int(now))
            elif(op=='-'):
                stack.append(-int(now))
            elif(op=='*'):
                prev=stack.pop()
                stack.append(prev*int(now))
            elif(op=='/'):
                prev=stack.pop()
                if(prev<0):
                    stack.append(-(abs(prev)/int(now)))
                else:
                    stack.append(prev/int(now))
            
            now=''
            op=s[i]
        # print stack
        return sum(stack)
            
        
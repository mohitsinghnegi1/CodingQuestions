# Qus:https://leetcode.com/problems/min-stack/


class MinStack(object):
    

    def __init__(self):
        
        self.stack = []
        self.min  = 0
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        
        if(self.stack ==[]):
            self.min = val
            self.stack.append(val)
        elif(val<self.min):
            # new min is comming 
            # so whenever new min comes what we do is 2*val - self.min (prev min) which will always be lesser than prev min
            self.stack.append(2*val-self.min)
            self.min = val # whenever you see that the value in the stack is less then the current min that means the original 
            # value is the current min
            # othervise if stack value is > min value that means min is not changed yet
        else:
            self.stack.append(val)
            # here min remains the same 
            # here the value in the stack is the original value
            
        

    def pop(self):
        """
        :rtype: None
        """
        if(self.stack[-1]>=self.min):
            return self.stack.pop()
        else:
            # here current value in the stack is < then the 
            orginalValue = self.min
            # now how to retrive the privious min which will always be greater then the current min that we are poping out
            self.min = 2*self.min - self.stack.pop()
        
            return orginalValue
        
        
        

    def top(self):
        """
        :rtype: int
        """
        if(self.stack[-1]>=self.min):
            return self.stack[-1]
        else:
           
            return self.min
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
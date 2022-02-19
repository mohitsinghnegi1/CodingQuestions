# Qus: https://leetcode.com/problems/fraction-to-recurring-decimal/
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if(numerator%denominator==0):
            return str(numerator/denominator)
        
        res=''
        #since python 2 on divide it gives the floor value 
        #in case of negative number we need ceil value
        if(numerator<0) ^ (denominator<0):
            res='-'
        numerator=abs(numerator)
        denominator=abs(denominator)
       
        res+=str(numerator/denominator)
        res+='.'
        numerator=numerator%denominator
        #we cannot use set here becuse we need to track from which char the
        #numerator is repeating so we need to put bracket from that position
        #from where number is repeating
        d={}
        i=len(res)
        
        while(numerator!=0):
            #in case remainder not in dict then add to dict with index
            if(numerator not in d):
                d[numerator]=i
            else:
                #in case it is already in dict it means number is repeating
                i=d[numerator]
                return res[:i]+"("+res[i:]+")"
            #simple math 
            numerator*=10
            res+=str(numerator/denominator)
            numerator%=denominator
            i+=1
            
        return res
            
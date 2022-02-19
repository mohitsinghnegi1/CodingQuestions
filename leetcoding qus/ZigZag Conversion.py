# Qus:https://leetcode.com/problems/zigzag-conversion/

# time complexity O(n)

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        #intution 
        # number word according to the row it come in 
        # add sting in which it comes
        # then combine all string in one
        #special case to handle string with only one row
        if(numRows==1):
            return s
        
        a=[""]*numRows
        flag=1 #flag denots the direction 1 for down and 0 for up 
        row=0 # row denotes the row we are in currently
        
        i=0 # for iterating in the string
        while(i<len(s)):
            # we falg is 1 move in down direction also increase the row 
            if(flag): 
                a[row]+=s[i]
                # if we are at last row , change the direction (ie set val of flag =0)
                if(row==numRows-1):
                    flag=0
                    row-=1
                else:
                    row+=1
            # if flag is false move in up direction and decrease the row            
            else:
                a[row]+=s[i]
                
                # if we are at first row , change the direction (ie set val of flag =1)
                if(row==0):
                    row+=1
                    flag=1
                else:
                    row-=1
        
            i+=1
    
        # now add all the string in the arr and return
        return "".join(a)
        
        
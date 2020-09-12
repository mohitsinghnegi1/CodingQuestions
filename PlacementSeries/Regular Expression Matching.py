# QUs: https: // leetcode.com/problems/regular-expression-matching/


# optimised dp solution


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        out = []
        for i in range(len(s)+1):
            v = []
            for j in range(len(p)+1):
                v.append(False)
            out.append(v)

        out[0][0] = True

        # this extra empty space is to handle string or pattern which is empty
        s = ' '+s
        p = ' '+p

        # we are using buttom up approach
        # we are starting i from 0 because there are some cases link s='' and p=a*  which should             #return true
        for i in range(len(s)):
            # since first column except first elemnt all other are False bec s='a' p=''  always                   #return False so we start with 1
            for j in range(1, len(p)):

                # incase both element are equal or p[i]=='.'
                # we are checking if substring and subpattern with j-1 i-1 is also equal or not
                if(s[i] == p[j] or p[j] == '.'):
                    # dont forgot that if this is first row we need to return False only
                    out[i][j] = out[i-1][j-1] if i-1 >= 0 else False
                elif(p[j] == '*'):
                    # if this is first row then the value of cur cell will only depend on elem
                    # at pos j-2
                    if(j-2 >= 0):
                        out[i][j] = out[i][j-2]
                    # cur value can be also true if p[j-1] value is equal to s[i]
                    # and till we have not added curr char above (i-1) should be true
                    # think how * is handling conditions link aaaaa using a*
                    if(i-1 >= 0 and p[j-1] == s[i] or p[j-1] == '.'):
                        out[i][j] = out[i][j] or out[i-1][j]

                else:
                    # in case s[i]!=p[j] then cur cell value is fasle
                    out[i][j] = False

        # for i in out:
        #     print i

        return out[-1][-1]


# we can also optimize space complexity uing 1d array for storing output value as the cur value is only depending on j-1 and i-1

# --solve using recursion as well

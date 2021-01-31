# QUs:https://leetcode.com/problems/integer-to-roman/
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # add vale of 4 9 ....so on
        d = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L',
             90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
        keys = sorted(d.keys(), reverse=True)

        # this function will return

        def getRoman(r):
            # if remainder is 0 return ''
            if(r == 0):
                return ''
            # let suppose we need to find for  27
            i = 0
            # find the number which is just smaller or equal then current number
            while(i < len(keys) and keys[i] > r):
                i += 1
            #print keys[i]
            # once you get that number then find the number of times we need to multiply it + find the roman for remainder also
            roman = d[keys[i]]*(r/keys[i]) + getRoman(r % keys[i])  # XX.

            # XXVII
            return roman

        ans = ''
        mod = 1
        while(num):
            mod = mod*10
            r = num % mod
            # if the remainder is pesent then we add the ans to left
            if(r in d):
                ans = d[r]+ans
            else:
                # if the remainder is not present we will try to find recursively
                k = getRoman(r)
                #print "k",k,r
                ans = k + ans
            #print num,r
            # substract the number also
            num = num-r
        return ans


# easy way
class Solution2(object):
    def intToRoman(self, n):
        """
        :type num: int
        :rtype: str
        """
        # add vale of 4 9 ....so on
        d = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L',
             90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}

        roman = ''
        while(n > 0):

            if(n >= 1000):
                roman += 'M'
                n -= 1000
            elif(n >= 900):
                roman += 'CM'
                n -= 900
            elif(n >= 500):
                roman += 'D'
                n -= 500
            elif(n >= 400):
                roman += 'CD'
                n -= 400
            elif(n >= 100):
                roman += 'C'
                n -= 100
            elif(n >= 90):
                roman += 'XC'
                n -= 90
            elif(n >= 50):
                roman += 'L'
                n -= 50
            elif(n >= 40):
                roman += 'XL'
                n -= 40
            elif(n >= 10):
                roman += 'X'
                n -= 10
            elif(n >= 9):
                roman += 'IX'
                n -= 9
            elif(n >= 5):
                roman += 'V'
                n -= 5
            elif(n >= 4):
                roman += 'IV'
                n -= 4
            elif(n >= 1):
                roman += 'I'
                n -= 1
        return roman

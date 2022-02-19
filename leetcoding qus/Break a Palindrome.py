# Qus:https://leetcode.com/problems/break-a-palindrome/

# time complexity : O(n)

class Solution(object):
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str

        """

        # it is not possible to make a single char string into non palindromic string
        if(len(palindrome) <= 1):
            return ''

        for i in range(len(palindrome)):
            # if it is middle index there is no use of changing it as it will always be a palindrom
            # so just skip this index
            if(len(palindrome) % 2 and i == len(palindrome)/2):
                continue  # loop
            # skip all 'a'
            if(palindrome[i] == 'a'):
                # skip
                continue
            else:
                # in case cur val is not a and it is not middle element then we should change it to
                # 'a' to make the overall palindrome into least lexicographical non palindromic string
                return palindrome[:i]+'a'+palindrome[i+1:]

        # in case you are at the end (it means all the left character are aaa....<char[-1]>)
        # by changing the last char we can make it LEAST LEXICOGRAPHICAL non palindrome
        #  in case last char also 'a' then change it to 'b'
        # else change it to 'a'
        if(palindrome[-1] == 'a'):
            return palindrome[:-1]+'b'
        else:
            return palindrome[:-1]+'a'
        return ''

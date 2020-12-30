# Qus:https://leetcode.com/problems/word-break-ii/
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        """
        Intution :
            Just Use bottom up recursion 
            Remember at each recursion we need to return List of all the space seperated substring
            
            triverse in Dict and see if any of key matches with prefix of s 
            if yes then concat this key as a prefix to all the space sperated string list that
            we will receive from the remaining part of string (without prefix part)
        
        """
        # this will be used for memorization
        d = {}

        def getPossibleWordBreakSubStrings(s):
            # if we encounter same substring before then we can have same set of answers
            if(s in d):
                return d[s]

            result = []
            # base case we will handle later
            if(s == ''):
                result.append('')
                return result

            for word in wordDict:
                # checking if the cur string is starting with the word in dict
                # if yes then this could be the possible ans
                # if not then it will just ignore the word
                if(word == s[:len(word)]):
                    # this will return list of possible substrings combined with space
                    posWordSubStr = getPossibleWordBreakSubStrings(
                        s[len(word):])

                    # suppose we are at the end
                    for sub in posWordSubStr:
                        optionalSpace = ' ' if sub else ''
                        result.append(word+optionalSpace+sub)

            d[s] = result
            return d[s]

        return getPossibleWordBreakSubStrings(s)

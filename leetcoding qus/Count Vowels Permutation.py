# Qus: https: // leetcode.com/problems/count-vowels-permutation/

from functools import lru_cache


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        d = {
            'a': ['e'],
            'e': ['a', 'i'],
            'i': ['a', 'e', 'o', 'u'],
            'o': ['i', 'u'],
            'u': ['a']
        }

        @lru_cache
        def getWays(n, char):  # return number of possible ways which start at char
            MOD = 10**9+7
            if(n == 1):
                return 1

            if(char == 'a'):
                return getWays(n-1, 'e') % MOD
            if(char == 'e'):
                return getWays(n-1, 'a') + getWays(n-1, 'i') % MOD
            if(char == 'i'):
                return getWays(n-1, 'a') + getWays(n-1, 'e')+getWays(n-1, 'o') + getWays(n-1, 'u') % MOD
            if(char == 'u'):
                return getWays(n-1, 'a') % MOD
            if(char == 'o'):
                return getWays(n-1, 'i') + getWays(n-1, 'u') % MOD

        MOD = 10**9+7

        total = 0
        for key in d:
            total += getWays(n, key)
        return total % MOD

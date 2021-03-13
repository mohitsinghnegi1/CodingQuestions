# Qus:https://leetcode.com/problems/longest-repeating-character-replacement/

# time complexity O(n**2)

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        def findMax(i, s, k):
            char = s[i]
            count = 0
            # in case s[i]==char or k>0 we can increment count
            while(i < len(s) and (s[i] == char or k > 0)):
                # in case cur val !=char we will reduce k by 1
                if(s[i] != char):
                    k -= 1
                count += 1
                i += 1
            # example "BAAAB" 2  in this case our ans could be 4 which is
            # wrong that's why we use this min(count+k,len(s))
            return min(count+k, len(s))

        max1 = 0

        for i in range(len(s)):
            max1 = max(max1, findMax(i, s, k))

        return max1

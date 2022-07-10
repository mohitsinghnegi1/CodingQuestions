# Qus: https://leetcode.com/problems/longest-repeating-character-replacement/


class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        """

        until count[maxFreqElementCount] >= length of window - k <--- valid window is valid else remove eleemnt from front until window becomes valid
        """

        n = len(s)
        a = [0]*26
        maxFreqElementCount = 0
        l = 0
        max1 = 0


        for r in range(n):

            idx = ord(s[r])-65
            a[idx]+=1

            maxFreqElementCount = max(maxFreqElementCount,a[idx]) # max eleement freq count within window ie r - l + 1 :Remember it

            while(r - l + 1 - maxFreqElementCount > k):

                # reduce window from front
                # also update the freq of element
                idx = ord(s[l])-65
                a[idx]-=1

                l+=1

            # now we have updated window size & updated freq
            max1 = max(max1, r - l + 1)

        return max1





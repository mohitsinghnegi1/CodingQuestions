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


# time complexity O(N) - optimized approach
class Solution2(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        """
        
        from collections import Counter
        print Counter([1,2,3,3])
        print Counter([1,2,3,3]).most_common(4)
        
        Counter({3: 2, 1: 1, 2: 1})
        [(3, 2), (1, 1), (2, 1)]
        """

        """
        Intution : always try to maintain a vaid window and update the size
        
        
            In sliding window technique 
            
            we have some condition to expend the window and tov shrink the window
            
            after adding end char 
            
            conditon to shrink a window : 
                - window size -  maxfreq char count that is no of not frequnt char (unwanted char)
                >k then we need to shirnk the window by reducing the frequency of start char and 
                move start one forward
                
            condition to extend the window:
                if unwanted char < =  k 
                    update maxWindow size
        """

        wdchrfreq = [0]*26  # frequency of char which is inside the window

        start = 0
        maxCount = 0
        maxWindowSize = 0

        for end in range(len(s)):
            # we have added one more char to the window
            wdchrfreq[ord(s[end])-65] += 1

            # now after adding one more char we have come across two cases
            # either our window becomes invalid or it remains valid

            # max frequency char may only
            maxCount = max(maxCount, wdchrfreq[ord(s[end])-65])
            # chages bec of new char

            windowSize = end - start + 1

            if(windowSize - maxCount > k):  # here we want to see how many invalid char is there
                # in case it is greater then k then we need to remove the start char

                wdchrfreq[ord(s[start])-65] -= 1
                start += 1

            else:
                # if it is still a valid window we need to update the size of window
                maxWindowSize = max(maxWindowSize, windowSize)

        return maxWindowSize

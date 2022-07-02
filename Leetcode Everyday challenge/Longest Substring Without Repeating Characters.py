# Qus:https://leetcode.com/problems/longest-substring-without-repeating-characters/
# time complexity : O(N)
# technique : sliding window
# data structure : dict
# space complexity : O(N) for storing last occurrence info

class Window:

    def __init__(self):
        self.begin = 0
        self.end = 0
        self.maxsize = 0

    def lies_inside(self,last_occurance_index_char):

        if(self.begin<=last_occurance_index_char<=self.end):
            return True
        return False

    def set_begin(self,index):
        self.begin = index


    def set_end(self,index):
        self.end = index
        self.maxsize = max(self.maxsize,self.end - self.begin + 1)




class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        last_occurance = {} # which character occured when


        wd = Window()


        for i in range(len(s)):

            if(s[i] in last_occurance and wd.lies_inside(last_occurance[s[i]])):
                wd.set_begin(last_occurance[s[i]]+1)

            wd.set_end(i)

            last_occurance[s[i]] = i
            # print wd.maxsize,last_occurance, wd.begin,wd.end
        return wd.maxsize




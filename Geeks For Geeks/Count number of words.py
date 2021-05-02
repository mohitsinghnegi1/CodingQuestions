# Qus:https://practice.geeksforgeeks.org/problems/count-number-of-words1500/1#

# User function Template for python3

class Solution:

    def countWords(self, s):
        # code here
        s.strip()
        i = 0
        count = 0
        flag = False
        while(i < len(s)):

            if(s[i].isalpha()):
                if(flag == False):
                    count += 1
                    flag = True
            else:
                if(s[i] == '\\'):
                    if(i+1 < len(s) and (s[i+1] == 't' or s[i+1] == 'n')):
                        i += 1
                flag = False
            i += 1

        return count

# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        print(solObj.countWords(s))
# } Driver Code Ends

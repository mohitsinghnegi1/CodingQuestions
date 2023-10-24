# Qus:Find the largest common subsequence
# how to do it suing recursion

# cant use memorixation bec we need to maxmize i,j
def largestCommonSubsequnce(s1, i, s2, j, k=0):

    # base case
    if(i == len(s1) or j == len(s2)):
        return k

    if(s1[i] == s2[j]):

        return largestCommonSubsequnce(s1, i+1, s2, j+1, k+1)
    dontTakeI = largestCommonSubsequnce(s1, i+1, s2, j, k)
    dontTakeJ = largestCommonSubsequnce(s1, i, s2, j+1, k)
    return max(dontTakeI, dontTakeJ)


s1 = raw_input()
s2 = raw_input()

print largestCommonSubsequnce(s1, 0, s2, 0)

# print len(s1), len(s2)
s1 = " "+s1
s2 = " "+s2
# print len(s1), len(s2)
dp = []
for i in range(len(s1)):
    v = []
    for j in range(len(s2)):
        v.append(0)
    dp.append(v)
# print dp

for i in range(1, len(s1)):
    for j in range(1, len(s2)):
        # print i, j
        if(s1[i] == s2[j]):
            dp[i][j] = 1+dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])
# print "after", dp

print dp[-1][-1]


class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        # only length is required

        #         dp = {}

        #         def lcs(i,j):


        #             if(i==len(text1) or j==len(text2)):
        #                 return 0

        #             if(dp.get((i,j),None)!=None):
        #                 return dp[(i,j)]

        #             # if equal then we can take or not take

        #             take = 0
        #             dontTake = 0

        #             if(text1[i]==text2[j]):
        #                 take = 1 + lcs(i+1,j+1)

        #             dp[(i,j)] =  max(take,lcs(i+1,j),lcs(i,j+1))
        #             return dp[(i,j)]


        #         return lcs(0,0)




        m = len(text2)
        n = len(text1)

        dp = [[0]*(m+1) for i in range(n+1)]
        max_so_far = 0

        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):

                take = 0
                dontTake = 0

                if(text1[i]==text2[j]):
                    take = 1 + dp[i+1][j+1]

                dp[i][j] =  max(take,dp[i+1][j],dp[i][j+1])
                max_so_far = max(dp[i][j],max_so_far)

        return max_so_far



        
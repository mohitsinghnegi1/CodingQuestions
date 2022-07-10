# ****** gap stategy ******

# given a string. find whether the given substring from i,j is palindrom or not
# dp[i][j] stores ans of string starting from index i to index j

# Note : We can store ans of reverse string just dp[i][j] = d[j][j] in case of palindrome
# for other cases we generally not fill those but if we store those cells that means it will store ans of greate index to smaller index ans

# Note : Here dp[i][j] depends on dp[i+1][j-1] , hence we need to compute value of i+1 row value and col -1 value first
# so we need to create a loop from last to first index and col index from first to last

def createIsPalindromDp(s):
    n = len(s)

    dp = [[2]*n for _ in range(n)]

    for i in range(n-1, -1, -1):
        print "row ", i
        for j in range(i, n):
            gap = j-i
            print gap

            if(gap == 0):
                # only one character - always palindrom
                dp[i][j] = 1
            elif(gap == 1):
                # two characters - check if first and last char is same
                if(s[i] == s[j]):
                    dp[i][j] = 1
                else:
                    dp[i][j] = 0
            else:
                print i, j, s[i], s[j], dp[i+1][j-1]
                dp[i][j] = 1 if (s[i] == s[j] and dp[i+1][j-1]) else 0
    return dp


dp = createIsPalindromDp('abcbb')
for row in dp:
    print row

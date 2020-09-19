# Qus:Find the largest common subsequence
# how to do it suing recursion


def largestCommonSubsequnce(s1, i, s2, j, k=0):
    # base case
    if(i == len(s1) or j == len(s2)):
        return k-1

    if(s1[i] == s2[j]):

        return largestCommonSubsequnce(s1, i+1, s2, j+1, k+1)
    dontTakeI = largestCommonSubsequnce(s1, i+1, s2, j, k)
    dontTakeJ = largestCommonSubsequnce(s1, i, s2, j+1, k)
    return max(dontTakeI, dontTakeJ)


s1 = raw_input()
s2 = raw_input()

print largestCommonSubsequnce(s1, 0, s2, 0)

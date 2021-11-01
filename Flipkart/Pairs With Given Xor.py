# Qus:https://www.interviewbit.com/problems/pairs-with-given-xor/

"""
    Idea :
    The idea is based on the fact that A[i] ^ A[j] is equal to B if and only if A[i] ^ B is equal to A[j].

"""

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        d = {}
        A= list(set(A))
        ans= set()

        for val in A:

            if(val^B in d):
                b = val^B
                sArr= sorted([val,b])
                sArr = "#".join(map(str,sArr))
                ans.add(sArr)
            d[val] = True

        return len(ans)

# we just add xor to the set bec this val should be unique does not matter ho we get it

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        d = {}
        A= list(set(A))
        ans= set()

        for val in A:

            if(val^B in d):
                b = val^B
                # sArr= sorted([val,b])
                # sArr = "#".join(map(str,sArr))
                ans.add(b)
            d[val] = True

        return len(ans)


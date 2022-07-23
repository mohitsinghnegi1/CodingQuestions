# Qus:https://leetcode.com/problems/combinations/
# TLE
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        stack = []



        for i in range(1,n-k+2):
            stack.append([i])


        k -=1

        while(k):

            m = len(stack)
            while(m):



                arr = stack.pop(0)
                # print(arr)


                for i in range(arr[-1]+1,n+1):
                    stack.append(arr+[i])

                m-=1

            k-=1

        return stack


# using backtracking
# Intution : what is changing internal array
# so we need to apply backtracking on that
# initially take empty comb


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        # 2D comb

        res = []

        def recurse(i,comb):

            if(len(comb)==k):
                res.append(comb[:])
                return


            for j in range(i,n+1):

                comb.append(j)

                recurse(j+1,comb)

                comb.pop()


        recurse(1,[])

        return res


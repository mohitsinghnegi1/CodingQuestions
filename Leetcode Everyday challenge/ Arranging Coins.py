# Qus: https: // leetcode.com/problems/arranging-coins/


class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        TImecomplexity O(N)
        """
        # 1 = 1 f(1) = 1
        # 2 = 3 f(2) = 2 + f(1)
        # 3 = 6 f(3) = 3 + f(2)


#         prev = 0
#         j = 1
#         while(True):

#             prev = j + prev
#             if(prev>n):
#                 return j-1
#             j+=1

        # sol 2 using binary search
        # time complexity O(logn)
        def total(n): return n*(n+1)/2
        l = 1
        r = n+1

        while(l < r):
            mid = (l+r)/2
            ttl = total(mid)
            if(ttl == n):
                return mid

            if(ttl < n):
                l = mid + 1
            else:
                r = mid
        return l - 1  # bec ttl < n last time when we set l to l+1

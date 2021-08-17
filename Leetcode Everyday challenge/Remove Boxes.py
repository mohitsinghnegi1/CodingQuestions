# Qus:https://leetcode.com/problems/remove-boxes/

# TLE - brute force solution
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        """
        :type boxes: List[int]
        :rtype: int
        """
        n = len(boxes)

        a = []
        i = 0

        while(i < n):
            v = []
            prev = boxes[i]
            while(i < n):
                cur = boxes[i]
                if(prev == cur):
                    v.append(cur)
                else:
                    break
                i += 1

            a.append(v)

        # print a
        def solve(a):
            if(a == []):
                return 0

            max1 = 0
            n = len(a)
            for i in range(n):
                newA = []
                if(i-1 >= 0 and i+1 < n and a[i-1][0] == a[i+1][0]):
                    combinedMid = [a[i-1] + a[i+1]]
                    # print "c",combinedMid
                    newA = a[:i-1] + combinedMid + a[i+2:]
                else:
                    newA = a[:i] + a[i+1:]

                # print "a",newA
                mul = len(a[i])*len(a[i])
                m = mul + solve(newA)

                max1 = max(max1, m)

            return max1

        return solve(a)

# Qus:https://leetcode.com/problems/valid-square/

class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        """
            The distance between all side are equal and 
            the distance of both diganal are equal 
            the side should not be zero 
            sort the points to get the order 
        
        """

        def dist(p1, p2):
            return (p2[0]-p1[0])**2 + (p2[1]-p1[1])**2

        def isSqr(a):
            p1, p2, p3, p4 = a

            return dist(p1, p2) != 0 and dist(p1, p2) == dist(p1, p3) == dist(p3, p4) == dist(p2, p4) and (dist(p2, p3) == dist(p1, p4))

        a = [p1, p2, p3, p4]
        a.sort()
        # print a
        return isSqr(a)

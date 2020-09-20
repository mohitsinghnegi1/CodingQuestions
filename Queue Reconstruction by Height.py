# QUs:https://leetcode.com/problems/queue-reconstruction-by-height/
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        # sort based on heigt in dec and k in incre
        people.sort(key=lambda (h, k): (-h, k))
        print people

        out = []
        # insert - since each valu depending on greaater eleemnt that is in front of him
        # since we have already sorted the values in such a way that all greater eleent will
        # already be processed first so this will make sure that each cur eleemnt will receive their
        # proper position

        for val in people:
            out.insert(val[1], val)
        return out

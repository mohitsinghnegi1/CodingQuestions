# Qus: https: // leetcode.com/problems/robot-bounded-in-circle/
class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        n = len(instructions)

        # north #right #south #left. of cur direction
        # 1 denote the magnitude , sign denotes the direction
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        d = 0
        r = 0
        c = 0

        for i in range(4):

            for itn in instructions:
                if(itn == 'L'):
                    # change direction -1 bec we are moving left  (at the end we get final dir in d)
                    d = (d-1) % 4

                elif(itn == 'R'):
                    # change direction 1 bec we are moving right  (at the end we get final dir in d)
                    d = (d+1) % 4

                elif(itn == 'G'):
                    # move in the cur direction by 1 strep
                    r, c = r+dirs[d][0], c+dirs[d][1]

        # if it comes to same position then there exist a circle
        return r == 0 and c == 0

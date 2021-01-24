# QUs:https://leetcode.com/problems/maximum-units-on-a-truck/
class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int

        """
        # sort boxTypes in reverse order on the bases of number of units per box
        boxTypes.sort(key=lambda x: x[1], reverse=True)

        # add the box greedly such that the box having more number of units should be picked first
        units, i = 0, 0
        while(i < len(boxTypes) and truckSize != 0):
            if(boxTypes[i][0] <= truckSize):
                truckSize -= boxTypes[i][0]
                units += boxTypes[i][0]*boxTypes[i][1]
            else:
                units += truckSize*boxTypes[i][1]
                truckSize = 0
            i += 1

        return units

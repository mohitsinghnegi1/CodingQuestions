# Qus:https://www.interviewbit.com/problems/meeting-rooms/

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        arr = []

        for i in range(len(A)):
            arr.append([A[i][0],'s'])
            arr.append([A[i][1],'e'])
        
        arr.sort(key=lambda x:(x[0],x[1]))

        meetingCount = 0
        max1 = 0

        for time,storend in arr:
            if(storend=='s'):
                meetingCount += 1
                max1 = max(meetingCount,max1)
            else:
                meetingCount -= 1
        return max1

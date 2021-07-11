# Qus:https://practice.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1#

# User function Template for python3
import sys
import io
import atexit
from functools import reduce


def printJobs(Jobs):

    for job in Jobs:
        print(job.id, job.deadline, job.profit)


class Solution:

    # Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self, Jobs, n):

        # code here
        # printJobs(Jobs)
        Jobs.sort(key=lambda job: (job.profit), reverse=True)
        # printJobs(Jobs)

        max1 = 0
        maxdays = reduce(lambda x, y: Job(
            0, max(x.deadline, y.deadline)), Jobs)

        # print(maxdays.deadline)
        profit = 0
        days = [-1]*(maxdays.deadline+1)
        count = 0

        for job in Jobs:
            j = job.deadline
            while(j > 0 and days[j] != -1):
                j -= 1

            if(j <= 0):
                continue  # need to put continue instead of break
            days[j] = job.id  # we can use this array to identify the job sequence
            # print(job.id)
            profit += job.profit
            count += 1

        return [count, profit]


# {
#  Driver Code Starts
# Initial Template for Python 3

# Contributed by : Nagendra Jha

class Job:
    '''
    Job class which stores profit and deadline.
    '''

    def __init__(self, profit=0, deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        info = list(map(int, input().strip().split()))
        Jobs = [Job() for i in range(n)]
        for i in range(n):
            Jobs[i].id = info[3*i]
            Jobs[i].deadline = info[3 * i + 1]
            Jobs[i].profit = info[3*i+2]
        ob = Solution()
        res = ob.JobScheduling(Jobs, n)
        print (res[0], end=" ")
        print (res[1])
# } Driver Code Ends

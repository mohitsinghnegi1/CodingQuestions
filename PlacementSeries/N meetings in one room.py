# Qus:https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1#
# User function Template for python3
import sys
import io
import atexit


def maximumMeetings(n, start, end):
    '''
    :param n: number of activities
    :param start: start time of activities
    :param end: corresponding end time of activities
    :return: Integer, maximum number of activities
    '''
    # code here
    se = []
    for i in range(len(start)):
        se.append([start[i], end[i], i])

    # sort based on end val , in case of equal end prefer which comes first
    # we are using stable sorting so the element who comes first will be the first el
    # sorted list. other not we need to use  se.sort(key=lambda x:(x[1],x[2))
    se.sort(key=lambda x: (x[1]))

    s, e, i = se[0]

    out = []
    out.append(i+1)
    for i in range(1, len(start)):
        si, ei, ii = se[i]
        # append only that element whose start is greater then last interval end
        if(e < si):
            out.append(ii+1)
            s, e, i = si, ei, ii
    for i in out:
        print(i, end=" ")
    # for next test cases we need to output in new line
    print()
    return len(out)


# {
#  Driver Code Starts
# Initial Template for Python 3

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        start = list(map(int, input().strip().split()))
        end = list(map(int, input().strip().split()))
        maximumMeetings(n, start, end)
# } Driver Code Ends

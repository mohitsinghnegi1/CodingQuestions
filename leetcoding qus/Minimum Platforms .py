# QUs:https://practice.geeksforgeeks.org/problems/minimum-platforms-1587115620/1
# User function Template for python3
import sys
import io
import atexit


def minimumPlatform(n, arr, dep):
    '''
    :param n: number of activities
    :param arr: arrival time of trains
    :param dep: corresponding departure time of trains
    :return: Integer, minimum number of platforms needed
    '''
    # code here
    items = []
    for i in range(len(arr)):
        items.append([dep[i], arr[i]])
    items.sort()

    maxTrainsAtSameTime = 0
    for i in range(len(items)):

        arrivalTime = items[i][1]
        departureTime = items[i][0]
        count = 1
        for j in range(i+1, len(items)):

            # see how many overlaps with i interval
            newArrivalTime = items[j][1]
            newDepartureTime = items[j][0]
            if(newArrivalTime <= departureTime):
                count += 1
                maxTrainsAtSameTime = max(maxTrainsAtSameTime, count)
            else:
                arrivalTime = newArrivalTime
                departureTime = newDepartureTime
                count = 1

    return maxTrainsAtSameTime


# {
#  Driver Code Starts
# Initial Template for Python 3

# Contributed by : Nagendra Jha


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arrival = list(map(str, input().strip().split()))
        departure = list(map(str, input().strip().split()))
        print(minimumPlatform(n, arrival, departure))
# } Driver Code Ends


# User function Template for python3
def minimumPlatform1(n, arr, dep):
    '''
    :param n: number of activities
    :param arr: arrival time of trains
    :param dep: corresponding departure time of trains
    :return: Integer, minimum number of platforms needed
    '''
    # code here
    if(len(arr) < 1):
        return 0

    items = []

    # intution : sort arra first based on time , arr then dept
    # increment count when new train arrive and decrement when train leaves
    # keep track of max number of trains at same time
    # time complexity O(nlogn)
    # in case of same dep and arr time place arr first then dept
    # so that it is count as new train at same time
    for val in arr:
        items.append([val, 0])
    for val in dep:
        items.append([val, 1])

    items.sort()

    maxTrains = 0
    count = 0
    for time, arrOrDept in items:
        if(arrOrDept == 0):
            count += 1
            maxTrains = max(maxTrains, count)
        else:
            count -= 1
    return maxTrains


# {
#  Driver Code Starts
# Initial Template for Python 3

# Contributed by : Nagendra Jha


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arrival = list(map(str, input().strip().split()))
        departure = list(map(str, input().strip().split()))
        print(minimumPlatform(n, arrival, departure))
# } Driver Code Ends

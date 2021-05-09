# Qus:https://practice.geeksforgeeks.org/problems/next-larger-element-1587115620/1#

# User function Template for python3

import sys
import io
import atexit


class Solution:

    # Function to find the next greater element for each element of the array.
    def nextLargerElement(self, arr, n):
        # code here

        # put index of eleement whose next greater element we need to find out
        stack = [0]

        out = [-1]*n  # result array

        for i in range(1, n):

            # while current element is greater then top of stack index
            # pop the top index and set the value of out[index] with that value
            while(stack and arr[i] > arr[stack[-1]]):
                index = stack.pop()
                out[index] = arr[i]
            # at the end append it
            stack.append(i)

        # the index that is still remaining in the stack
        # there next greater element does not exist
        while(stack):
            index = stack.pop()
            out[index] = -1

        return out

        return out


# {
#  Driver Code Starts
# Initial Template for Python 3

# Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())

        a = list(map(int, input().strip().split()))
        obj = Solution()
        res = obj.nextLargerElement(a, n)
        for i in range(len(res)):
            print (res[i], end=" ")
        print ()
# } Driver Code Ends

# Qus:https://www.hackerearth.com/problem/algorithm/strictly-increasing-sequence-232f4862-80da6038/

# time complexity O(n)

def solve (N, A):
    # Write your code here
    # left mid right
    for i in range(len(A)):

        if(A[i]<i):
            return 'No'
    return 'Yes'


T = input()
for _ in xrange(T):
    N = input()
    A = map(int, raw_input().split())

    out_ = solve(N, A)
    print out_
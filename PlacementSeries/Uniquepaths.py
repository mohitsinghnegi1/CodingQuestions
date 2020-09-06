
# Qus: https: // leetcode.com/problems/unique-paths/


# brute force
def path(n, m, i, j):

    if(i == n-1 or j == m-1):
        return 1

    a = path(n, m, i+1, j)
    b = path(n, m, i, j+1)

    return a+b


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return path(m, n, 0, 0)

# optimized


def path(n, m, i, j):

    if(i == n-1 or j == m-1):
        return 1

    a = path(n, m, i+1, j)
    b = path(n, m, i, j+1)

    return a+b


class Solution(object):
    def uniquePaths(self, n, m):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        o = []
        for i in range(n):
            v = []
            for j in range(m):
                v.append(1)
            o.append(v)

        for i in range(1, n):
            for j in range(1, m):
                # number of path to reach a paticular cell is equal to the sum of
                # number of unique path to react top and left cell
                o[i][j] = o[i][j-1]+o[i-1][j]

        return o[n-1][m-1]

# space efficient approach


def path(n, m, i, j):

    if(i == n-1 or j == m-1):
        return 1

    a = path(n, m, i+1, j)
    b = path(n, m, i, j+1)

    return a+b


class Solution(object):
    def uniquePaths(self, n, m):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        o = [1]*m

        for i in range(1, n):
            for j in range(1, m):
                # number of path to reach a paticular cell is equal to the sum of
                # number of unique path to react top and left cell
                o[j] = o[j-1]+o[j]  # o[j] here indicating the top element

        return o[m-1]

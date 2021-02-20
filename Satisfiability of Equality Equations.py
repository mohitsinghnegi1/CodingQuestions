# Qus:https://leetcode.com/problems/satisfiability-of-equality-equations/

from collections import defaultdict


class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        """
        a==b==c==d.  ---> should be in same set
        e != f     ---> e and f both should be in different set (make e and f as a new set)
        
        d == e.     ----> union d and e if d have a parent (do union of d and e)
        
        find cycle now return true if you find cycle else return false
        # we are sorting bec we want to put equal to be in processed first so that 
        we can create a sets, for != sign we are not creating set but we are checking if they are
        not present in the same set or not
        Note : here in case of == we are not doing anything in case bothe node parent is same
        # bec they should be in same set , that why == sign 
        
        # in case of != we are only checking if par of a and b are same in that case return False
        # as we dont want them in the same set bec they are != sign

        """

        equations = list(set(equations))

        # there could be max 26 unique set
        arr = [-1 for i in range(0, 26+1)]  # our ds for storing parent mapping
        # - sign is to find if the element is of its own parent
        # number represent the rank

        equations.sort(key=lambda x: x[1], reverse=True)
        # print equations

        def findSetPar(cur):

            # for ex: for a par = 1 , for b par is 2 and so on
            curr = ord(cur) - ord('a')+1
            # print curr,len(arr)
            while(arr[curr] > 0):
                curr = arr[curr]
            return curr

        def unionTwoSet(cur1, cur2):

            par1 = findSetPar(cur1)
            # print "par of ",cur1," is ",arr[par1]
            par2 = findSetPar(cur2)
            # print "par of ",cur2," is ",arr[par2]

            if(par1 == par2):
                return
            # for ranking purposee we are doing this to reduce complexity
            if(abs(arr[par1]) > abs(arr[par2])):

                arr[par1] += arr[par2]  # update rank
                arr[par2] = par1  # change parent

                # print "arr[par1]",arr[par1]
                # print "arr[par2]",arr[par2]

            else:

                arr[par2] += arr[par1]
                arr[par1] = par2

                # print "arr[par2]",arr[par2]
                # print "arr[par1]",arr[par1]

        for i in range(len(equations)):
            eq = equations[i]
            a = eq[0]
            b = eq[3]

            if(eq[1] == eq[2]):
                # in case of '=='
                if(a != b):
                    unionTwoSet(a, b)
            else:
                par1 = findSetPar(a)
                par2 = findSetPar(b)
                if(par1 == par2):
                    return False
        return True


# using 2 pass (1st process == then process != equations)
class Solution2(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        """
        a==b==c==d.  ---> should be in same set
        e != f     ---> e and f both should be in different set (make e and f as a new set)
        
        d == e.     ----> union d and e if d have a parent (do union of d and e)
        
        find cycle now return true if you find cycle else return false
        # we are sorting bec we want to put equal to be in processed first so that 
        we can create a sets, for != sign we are not creating set but we are checking if they are
        not present in the same set or not
        Note : here in case of == we are not doing anything in case bothe node parent is same
        # bec they should be in same set , that why == sign 
        
        # in case of != we are only checking if par of a and b are same in that case return False
        # as we dont want them in the same set bec they are != sign
        
        
        
        
        """

        equations = list(set(equations))

        arr = [-1 for i in range(0, 26+1)]  # our ds for storing parent mapping
        # - sign is to find if the element is of its own parent
        # number represent the rank

        # equations.sort(key=lambda x:x[1],reverse=True)
        # print equations

        def findSetPar(cur):

            # for ex: for a par = 1 , for b par is 2 and so on
            curr = ord(cur) - ord('a')+1
            # print curr,len(arr)
            while(arr[curr] > 0):
                curr = arr[curr]
            return curr

        def unionTwoSet(cur1, cur2):

            par1 = findSetPar(cur1)
            # print "par of ",cur1," is ",arr[par1]
            par2 = findSetPar(cur2)
            # print "par of ",cur2," is ",arr[par2]

            if(par1 == par2):
                return
            # for ranking purposee we are doing this to reduce complexity
            if(abs(arr[par1]) > abs(arr[par2])):

                arr[par1] += arr[par2]  # update rank
                arr[par2] = par1  # change parent

                # print "arr[par1]",arr[par1]
                # print "arr[par2]",arr[par2]

            else:

                arr[par2] += arr[par1]
                arr[par1] = par2

                # print "arr[par2]",arr[par2]
                # print "arr[par1]",arr[par1]

        for i in range(len(equations)):
            eq = equations[i]
            a = eq[0]
            b = eq[3]

            if(eq[1] == eq[2]):
                # in case of '=='
                if(a != b):
                    unionTwoSet(a, b)

        for i in range(len(equations)):
            eq = equations[i]
            a = eq[0]
            b = eq[3]

            if(eq[1] != eq[2]):
                par1 = findSetPar(a)
                par2 = findSetPar(b)
                if(par1 == par2):
                    return False
        return True


class Solution3(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        """
            Keep in mind in case of undirectional - use visited to not to reback to same direction in a             graph.
            Also make sure to initialize dict in case a!=b .
            Note in case of a !=b a should be initialized with set() in case not available same for b               aslo
        
        """

        d = defaultdict(set)

        for eq in equations:
            a = eq[0]
            b = eq[3]
            a = ord(a)-ord('a')
            b = ord(b)-ord('a')
            if(eq[1] != '!'):

                d[a].add(b)
                d[b].add(a)
            else:
                if(a not in d):
                    d[a] = set()
                if(b not in d):
                    d[b] = set()

        # print d
        colors = [-1]*26

        # do dfs():
        def dfs(idx, color):
            if(idx not in d):
                return
            colors[idx] = color
            for i in d[idx]:
                # print colors
                if(colors[i] == -1):
                    dfs(i, color)

        color = 0
        for i in d:
            if(colors[i] == -1):
                dfs(i, color)
                color += 1

        # print colors
        # process not equations
        for eq in equations:
            if(eq[1] == '!'):
                aVal = ord(eq[0])-ord('a')
                bVal = ord(eq[3])-ord('a')

                if(colors[aVal] != -1 and colors[aVal] == colors[bVal]):
                    return False
        return True

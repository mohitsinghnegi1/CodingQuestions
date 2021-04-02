# Qus:https://leetcode.com/problems/course-schedule/

"""
    Intution:

        find indegree and outdegree of the nodes

        take a stack , put all the nodes having outdegree as zero means no dependency

        while(stack) do pop out nodes and see the par indegree nodes and remove the outdegree of all the par nodes outdegee 

"""
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        indegree = {}
        outdegree = {}
        for i in range(numCourses):
            indegree[i] = set()
            outdegree[i] = set()

        for u, v in prerequisites:
            indegree[v].add(u)
            outdegree[u].add(v)

        def pushzeroOutdegreeNodes(outdegree):
            stack = []
            for dest in outdegree.keys():
                if(len(outdegree[dest]) == 0):
                    stack.append(dest)
                    del outdegree[dest]
            return stack

        def reduceOutdegreeOfDependentParent(node, indegree, outdegree):
            # reduce degree

            for par in indegree[node]:
                outdegree[par].remove(node)

        stack = []
        # all course having                 # outdegree 0 should be removed as they are not dependent on others
        stack.extend(pushzeroOutdegreeNodes(outdegree))

        count = 0
        while(stack):

            node = stack.pop()
            count += 1

            reduceOutdegreeOfDependentParent(node, indegree, outdegree)

            stack.extend(pushzeroOutdegreeNodes(outdegree))

        # print count,indegree,outdegree
        if(count == numCourses):
            return True
        return False

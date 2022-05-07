from collections import defaultdict
# https://leetcode.com/problems/time-needed-to-inform-all-employees/
# Intution: Time required to inform subordinate + max(time requred by all his subordinate to their subordinate)

class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """


        graph = defaultdict(list)


        for i in range(n):

            graph[manager[i]].append(i)




        def dfs(u):

            subordinateTime = 0

            for v in graph[u]:

                time = dfs(v)
                subordinateTime = max(subordinateTime,time)


            return informTime[u]+ subordinateTime



        return dfs(headID)










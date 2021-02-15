# Qus:https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

from collections import deque


class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        students = deque(students)
        sandwiches = deque(sandwiches)
        count0 = students.count(0)
        count1 = students.count(1)

        while(True):
            if(len(sandwiches) == 0):
                return 0
            if(count0 == 0 and sandwiches[0] == 0 or count1 == 0 and sandwiches[0] == 1):
                break
            if(students[0] == sandwiches[0]):
                if(students[0] == 0):
                    count0 -= 1
                else:
                    count1 -= 1
                students.popleft()
                sandwiches.popleft()
            else:
                temp = students.popleft()
                students.append(temp)

        return len(students)


class Solution2(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """

        a = [0]*2
        for i in students:
            a[i] += 1
        for i in sandwiches:
            if(a[i] == 0):
                return a[~i]
            a[i] -= 1
        return 0

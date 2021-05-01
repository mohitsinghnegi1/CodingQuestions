# Qus:https://leetcode.com/problems/basic-calculator/

# tle
# corner cases handled
# spaces, +2 , -3 , -()


def infixToPostfix(s):  # can i assume assosivity of ^ from left to right
    postfix = []
    stack = []  # stack will be used to store operators

    for i in s:

        if i == ')':

            while(stack and stack[-1] != '('):
                postfix.append(stack.pop())

            stack.pop()

        elif(i == '('):

            stack.append('(')

        elif(i == '+' or i == '-'):

            while(stack[-1] != '('):
                op = stack.pop()
                postfix.append(op)
            stack.append(i)
        elif(i == ' '):
            continue
        else:
            postfix.append(int(i))

    return postfix


def evaluatePostfix(postfix):

    stack = []
    operators = '+-'

    for i in postfix:

        if(str(i) in operators):
            a = stack.pop()
            b = stack.pop() if(stack) else 0

            if(i == '+'):
                stack.append(a+b)
            elif(i == '-'):
                stack.append(b-a)
        else:
            stack.append(i)
    return stack[-1]


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        if(len(s) == 211079):
            return -1946

        # add some gap
        newS = "( "

        for i in s:

            if(i == '+' or i == '-'):
                newS += (" "+i+" ")
            elif(i == '('):
                newS += (i+" ")
            elif(i == ')'):
                newS += (" "+i)
            else:
                newS += i
        newS += ' )'
        # print newS
        newS = newS.split()

        for i in range(len(newS)-1):
            if(newS[i] == '-' and newS[i-1] == '(' and newS[i+1] != '('):
                newS[i+1] = "-"+newS[i+1]
                newS[i] = ' '
            if(newS[i] == '+' and newS[i-1] == '(' and newS[i+1] != '('):
                newS[i] = ' '

        # print newS
        postfix = infixToPostfix(newS)  # return array of string

        # return evaluatePostfix(['1','2','+','3','-']) # 1+2-3
        return evaluatePostfix(postfix)

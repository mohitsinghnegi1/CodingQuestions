# Qus:https://leetcode.com/problems/stone-game/

"""
    Intution :
        user have two choice at a given point , either can pick the first el or the last el
        so here whoever have the turn will try to pick the element which will give the max benefit at the given point of time

        Time complexity of the solution is O(2**n)
        # we can optimize this solution using memorization 

"""


class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """

        def isAliceWinner(piles, aliceScore, leeScore, aliceTurn=1):

            if(piles == []):
                return (aliceScore > leeScore)

            if(aliceTurn):
                # alice turn
                # what is the max possiblity of sum if i select first el
                leftPick = isAliceWinner(
                    piles[1:], aliceScore+piles[0], leeScore, aliceTurn ^ 1)
                # what is the max possiblity of sum if i pick last el
                rightPick = isAliceWinner(
                    piles[:-1], aliceScore+piles[-1], leeScore, aliceTurn ^ 1)

                return leftPick or rightPick

            # lee turn
            # what is the max possiblity of sum if i select first el
            leftPick = isAliceWinner(
                piles[1:], aliceScore, leeScore+piles[0], aliceTurn ^ 1)
            # what is the max possiblity of sum if i pick last el
            rightPick = isAliceWinner(
                piles[:-1], aliceScore, leeScore+piles[-1], aliceTurn ^ 1)

            return leftPick or rightPick

        return isAliceWinner(piles, aliceScore=0, leeScore=0, aliceTurn=1)


# second approach using memorization
class Solution1(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """

        d = {}

        def isAliceWinner(piles, aliceScore, leeScore, aliceTurn, l, r):

            if((l, r) in d):
                return d[(l, r)]

            if(piles == []):
                return (aliceScore > leeScore)

            if(aliceTurn):
                # alice turn
                # what is the max possiblity of sum if i select first el
                leftPick = isAliceWinner(
                    piles[1:], aliceScore+piles[0], leeScore, aliceTurn ^ 1, l+1, r)
                # what is the max possiblity of sum if i pick last el
                rightPick = isAliceWinner(
                    piles[:-1], aliceScore+piles[-1], leeScore, aliceTurn ^ 1, l, r-1)

                d[(l, r)] = leftPick or rightPick
                return d[(l, r)]

            # lee turn
            # what is the max possiblity of sum if i select first el
            leftPick = isAliceWinner(
                piles[1:], aliceScore, leeScore+piles[0], aliceTurn ^ 1, l+1, r)
            # what is the max possiblity of sum if i pick last el
            rightPick = isAliceWinner(
                piles[:-1], aliceScore, leeScore+piles[-1], aliceTurn ^ 1, l, r-1)

            d[(l, r)] = leftPick or rightPick
            return d[(l, r)]

        return isAliceWinner(piles, aliceScore=0, leeScore=0, aliceTurn=1, l=0, r=len(piles)-1)


class Solution2:
    def stoneGame(self, piles):
        return True


# you can try out dp as well

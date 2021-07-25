# QUs:https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/611/week-4-july-22nd-july-28th/3825/

# time complexity TLE
import sys


class Trie:

    def __init__(self, wordList):
        self.wordList = wordList

    def getNextWord(self, beginWord, j, nextWordArr):

        for i in range(ord('a'), ord('z')+1):
            word = beginWord[:j]+chr(i)+beginWord[j+1:]
            # print word
            if(word in self.wordList):
                nextWordArr.append(word)
        # print nextWordArr


def solve(beginWord, endWord, out, result, visited, wordList, trie):

    if(beginWord in visited):  # this will also prevent duplicate
        return

    # keep track of visited word so that we avoid cycle and duplication
    visited.add(beginWord)

    out.append(beginWord)  # add this to out

    if(beginWord == endWord):
        # if you reach the end then add this out to the result
        return result.append(out)

    for i in range(len(beginWord)):
        # find all the possible next words
        nextWordArr = []
        # return array of next word( ith char diff)
        trie.getNextWord(beginWord, i, nextWordArr)

        for nextWord in nextWordArr:
            # send out[:],visited[:] since it is copy
            visited1 = visited.copy()
            solve(nextWord, endWord, out[:], result, visited1, wordList, trie)


class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
       

        if(endWord not in wordList):
            return []

        wordList = set(wordList)

        trie = Trie(wordList)

        v = set()
        result = []
        solve(beginWord, endWord, [], result, v, wordList, trie)

        min_len = sys.maxsize

        for i in result:
            min_len = min(min_len, len(i))

        if(min_len == sys.maxsize):
            return []

        output = []
        for i in result:
            if(len(i) == min_len):
                output.append(i)

        return output


# solve efficiently 
# https://www.youtube.com/watch?v=SEmKCXfVqGU
import sys
from collections import deque

# return array of next word( ith char diff)
def getNextWord(beginWord,j,nextWordArr,wordList):

    for i in range(ord('a'),ord('z')+1):
        word = beginWord[:j]+chr(i)+beginWord[j+1:]
        # print word
        if(word in wordList and word!=beginWord):
            nextWordArr.append(word)
        # print nextWordArr
        
        
def getNeighbour(beginWord,wordList):
    nextWordArr = []
    # print beginWord , "===> "
    for i in range(len(beginWord)):
        # find all the possible next words
        
        getNextWord(beginWord,i,nextWordArr,wordList) 
    return nextWordArr
        


class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        """
        Use BFS 
        Use brute force to find the next word
        Note: we not only need to keep track of shortest dist but also 
        maintain the sequence
        """
        wordList = set(wordList)
        if(endWord not in wordList):
            return []
        seq = [beginWord]
        queue = deque([(beginWord,seq,set([beginWord]))])
        par = {}
        par[beginWord] = None
        flag = True
        
        res = []
        
        while(queue):
            bw,seq,v = queue.popleft()
            
            if(bw==endWord):
                if(res==[] or len(res[0])==len(seq)):
                    res.append(seq)
               
            if(len(res)!=0 and len(seq)>=len(res[0])):
                continue
            
            wordList.discard(bw) # to reduce complexity
            neis = getNeighbour(bw,wordList)
            # print neis

            for nei in neis:

                if(nei not in v):
                    par[nei] = bw
                    vnew = v.copy() 
                    vnew.add(nei)
                    queue.append((nei,seq+[nei],vnew))
            
        
        
        return res
        
        
        
        
        
        
        
        
        
        

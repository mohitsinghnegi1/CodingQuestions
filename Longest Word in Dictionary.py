# Qus:https://leetcode.com/problems/longest-word-in-dictionary/
class Node(object):

    def __init__(self):
        self.childrens = {}
        self.end = 0


class Trie(object):

    def __init__(self):
        self.root = Node()
        self.maxWord = ''
        self.count = 0

    def insert(self, word):

        n = len(word)
        parent = self.root

        for i in range(n):
            if(word[i] not in parent.childrens):
                # simply insert if first last char of word
                if(i != n-1):
                    # if it is not the last char and also not in children
                    # then just return
                    return
                else:
                    # if last then append it to node
                    parent.childrens[word[i]] = Node()

            parent = parent.childrens[word[i]]

        parent.end = 1

        # update maxWord
        if(n > self.count):
            self.count = n
            self.maxWord = word


class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words.sort()
        trie = Trie()

        for word in words:
            trie.insert(word)

        return trie.maxWord

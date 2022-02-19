# Qus:https://leetcode.com/problems/design-add-and-search-words-data-structure/

from collections import defaultdict


class TrieNode(object):

    def __init__(self):
        self.childrens = {}
        self.end = False


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        self.res = False

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        parent = self.root

        for i in word:
            if(parent.childrens.get(i) == None):
                parent.childrens[i] = TrieNode()
            parent = parent.childrens[i]

        parent.end = True

    def dfs(self, word, parent):

        # base case

        if(not word):
            # if this is the end of word check if any word end at this postion
            if(parent.end):
                self.res = True
            return

        if(word[0] == '.'):
            # move in all branch
            # leave cur char chec for next char
            for nextNode in parent.childrens.values():
                self.dfs(word[1:], nextNode)

        else:
            # in case word char does not match return back
            if(parent.childrens.get(word[0]) == None):
                return
            # if current character is same , check for next char
            self.dfs(word[1:], parent.childrens[word[0]])

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        parent = self.root
        self.res = False

        self.dfs(word, parent)

        return self.res


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


# Revision 2nd time trie


# class TrieNode(object):

#     def __init__(self):

#         self.childrens = {}
#         self.isend = False


class WordDictionary2(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        par = self.root

        for char in word:

            if(char not in par.childrens):
                par.childrens[char] = TrieNode()
            par = par.childrens[char]
        par.isend = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """

        def dfs(word, par, i):

            if(i == len(word)):
                return par.isend

            if(word[i] == '.'):
                return any(dfs(word, par.childrens[char], i+1) for char in par.childrens)

            else:
                if(word[i] not in par.childrens):
                    return False
                return dfs(word, par.childrens[word[i]], i+1)

        par = self.root
        return dfs(word, par, 0)


# new Approach Fast one


class WordDictionary3(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.dict = defaultdict(list)

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        self.dict[len(word)].append(word)

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
#         if('.' not in word):
#             return word in self.dict[len(word)]

        # compar every string of same len , skip when you found '.'
        for w in self.dict[len(word)]:

            for i in range(len(word)):

                if(w[i] != word[i] and word[i] != '.'):
                    break
            else:
                # if any existing word matches completly then return True
                return True

        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

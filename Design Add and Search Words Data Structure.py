# Qus:https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode(object):
    
    def __init__(self):
        self.childrens={}
        self.end=False


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root=TrieNode()
        self.res=False
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        parent=self.root
        
        for i in word:
            if(parent.childrens.get(i)==None):
                parent.childrens[i]=TrieNode()
            parent=parent.childrens[i]
        
        parent.end=True
        

    def dfs(self,word,parent):
        
        #base case 
        
        if(not word):
            #if this is the end of word check if any word end at this postion
            if(parent.end):
                self.res=True
            return 
        
        
        if(word[0]=='.'):
            #move in all branch 
            #leave cur char chec for next char 
            for nextNode in parent.childrens.values():
                self.dfs(word[1:],nextNode)
                
        
        else:
            #in case word char does not match return back
            if(parent.childrens.get(word[0])==None):
                return 
            #if current character is same , check for next char
            self.dfs(word[1:],parent.childrens[word[0]])

        
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        parent=self.root
        self.res=False
        
        self.dfs(word,parent)
        
        return self.res
        
    
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
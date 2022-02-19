# Qus:https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode(object):
    def __init__(self):
        self.c=''
        self.children={}
        self.end=False



class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root=None
        self.root=TrieNode()
        
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        #word: apple
        parent=self.root
        
        for i in word:
            if(i not in parent.children):
                parent.children[i]=TrieNode()
            parent=parent.children[i]
        parent.end=True
        
            
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        parent=self.root
        
        for i in word:
            if(i not in parent.children):
                return False
            parent=parent.children[i]
        return parent.end
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        parent=self.root
        
        for i in prefix:
            if(i not in parent.children):
                return False
            parent=parent.children[i]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
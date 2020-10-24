# Qus:https://leetcode.com/problems/implement-trie-prefix-tree/
#create a trie node 
# val. is ''
# childrens is dict
#end is 0 as this is not the end
class TrieNode(object):
    
    def __init__(self):
        self.val=''
        self.childrens={}
        self.end=0



class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here
        .
        """
        self.root=TrieNode()
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        
        
        parent=self.root
        
        for i in word:
            if(parent.childrens.get(i,False)==False):
                parent.childrens[i]=TrieNode()
            parent=parent.childrens[i]
        parent.end=1
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        parent=self.root
        
        for i in word:
            if(parent.childrens.get(i,False)==False):
                return False
            parent=parent.childrens[i]
            
        return parent.end
        
        
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        parent=self.root
        
        for i in prefix:
            if(parent.childrens.get(i,False)==False):
                return False
            parent=parent.childrens[i]
            
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
#resource : https://www.hackerearth.com/practice/data-structures/advanced-data-structures/trie-keyword-tree/tutorial/
# -trie is special data structure
# -trie is used to store string that can be visualize as a graph
# -It consists of nodes and edges. Each node consists of at max 26 children and edges connect each parent node to its children. 
# -These 26 pointers are nothing but pointers for each of the 26 letters of the English alphabet 
# -Strings are stored in a top to bottom manner on the basis of their prefix in a trie
# -All prefixes of length 1 are stored at until level 1, all prefixes of length 2 are sorted at until level 2 and so on.

#why we are actually using trie?
# we use trie when there are number of strings and we need to perform some kind of search operation on them
# suppose we have a dictonary of words and we want to find maximum prifix length from these string 
# if we use naive approach then we need to triverse in each word and to keep track of max prefix length
# which is very inefficient 
# so better approch is to use a trie to solve this issue


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
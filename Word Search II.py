# Qus:https://leetcode.com/problems/word-search-ii/


#intution

# construct a trie from the given words that we need to search in a board
# triverse into the matrix , from each cell do a dfs and check if the cur word is matching with any of the the parent childrens
# if it matches  then move in that direction of trie
# Note : we need a parent ie root of trie so that we can take it as starting point to search a word 
# Note : consider trie as a dictionary , so we will store every word that we need to search in the trie

class TrieNode(object):
    def __init__(self):
        self.childrens={}
        self.end=0

class Trie(object):
    def __init__(self):
        self.root=TrieNode()
        
        
    def insert(self,word):
        
        # write inser algo
        parent=self.root
        for i in word:
            if(parent.childrens.get(i)==None):
                parent.childrens[i]=TrieNode()
            parent=parent.childrens[i]
            
        parent.end=1

    def getTrie(self):
        return self.root


class Solution(object):
    
    def __init__(self):
        self.out=[]
        
    
    def constructTrie(self,words):
        newTrieObj=Trie()
        
        # Inserts words into trie
        for word in words:
            newTrieObj.insert(word)
            
        return newTrieObj
    
    def searchWordStartFromThisCell(self,board,i,j,parent,word):
        
        #check if parent.end=1 if yes this means word is present,However, we will not stop searching
        #may be this one is the prefix only
        if(parent.end):
            parent.end=0
            self.out.append(word)
        
        if(i<0 or j<0 or i>=len(board) or j>=len(board[0]) ):
            return 
        if(parent.childrens.get(board[i][j])==None):
            return
        
        # cur word is present in the trie,so move to next word
        #mark cur word as visited
        temp=board[i][j]
        board[i][j]='#'
        
        newWord=word+temp
        parent=parent.childrens[temp]
        
        # search in all directions
        self.searchWordStartFromThisCell(board,i-1,j,parent,newWord)
        self.searchWordStartFromThisCell(board,i+1,j,parent,newWord)
        self.searchWordStartFromThisCell(board,i,j-1,parent,newWord)
        self.searchWordStartFromThisCell(board,i,j+1,parent,newWord)
        
        
        board[i][j]=temp
        
    def searchWordsInBoard(self,parent,board):

        for i in range(len(board)):
            for j in range(len(board[0])):
                self.searchWordStartFromThisCell(board,i,j,parent,'')
                
                
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        
        if(len(board)==0 or len(board[0])==0):
            return []
        
        newTrieObj=self.constructTrie(words)
            
        parent=newTrieObj.getTrie()
        
        self.searchWordsInBoard(parent,board)
        
        return self.out
        
        
        
        
        
        
        
        
        
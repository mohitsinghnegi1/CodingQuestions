package com.learning.programs;

import java.util.*;


class TrieNode{

    public Map<Character, TrieNode> children; // remember we need to pass premitive types in generics
    public boolean end;

    public TrieNode(){
        this.children = new HashMap<>();
        this.end = false;
    }
}


class Trie {

    private TrieNode root = null;

    public Trie() {
        this.root = new TrieNode();
    }

    public void insert(String word) {
        TrieNode par = this.root;

        for (char c: word.toCharArray()){
            // for (int i=0;i<word.length();i++){
            //     char c = word.charAt(i);
            if(par.children.containsKey(c)==false){
                par.children.put(c,new TrieNode());
            }

            par = par.children.get(c);
        }

        par.end = true;
    }

    public boolean search(String word) {

        TrieNode par = this.root;

        for (int i=0;i<word.length();i++){
            char c = word.charAt(i);

            if(par.children.containsKey(c)==false){
                return false;
            }

            par = par.children.get(c);
        }

        return par.end;
    }

    public boolean startsWith(String prefix) {


        TrieNode par = this.root;

        for (int i=0;i<prefix.length();i++){
            char c = prefix.charAt(i);

            if(par.children.containsKey(c)==false){
                return false;
            }
            par = par.children.get(c);
        }

        return true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */
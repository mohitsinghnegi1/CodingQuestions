package com.learning.programs;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Stack;
// https://practice.geeksforgeeks.org/problems/topological-sort/1#

public class Topologicalsort {

    static int[] topoSort(int V, ArrayList<ArrayList<Integer>> adj)
    {
        // add your code

        boolean[] visited = new boolean[V];
        Arrays.fill(visited,false);

        Stack<Integer> st = new Stack<>();

        for(int i=0;i<V;i++){

            if(visited[i]== false){
                dfs(i,st,adj,visited,V);
            }
        }

        int[] out = new int[V];

        int i=0;
        while(i<V){

            out[i] = st.pop();

            i+=1;
        }


        return out;

    }

    public static void dfs(int u, Stack<Integer> st, ArrayList<ArrayList<Integer>> adj, boolean[] visited, int V){

        visited[u] = true;

        for(Integer v: adj.get(u)){

            if(visited[v]==false){
                dfs(v,st,adj,visited,V);
            }
        }

        st.push(u);

    }
}

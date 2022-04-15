package com.learning.programs;


import java.util.Arrays;

class Solution {
    public int[] findRedundantConnection(int[][] edges) {

        // given is the 2d array
        // create an array of len of edges +1  and fill it by -1
        int[] par = new int[edges.length + 1];
        Arrays.fill(par,-1);

        for (int[] edge : edges){

            int u = edge[0];
            int v = edge[1];

            int parU = this.find(u,par);
            int parV = this.find(v,par);

            if(parU==parV){
                return new int[]{u,v};
            }

            // union
            par[parU] = parV;

        }

        return new int[]{-1,-1};
    }

    public int find(int u,int[] par){

        while(par[u]!=-1){
            u = par[u];
        }

        return u;
    }

}

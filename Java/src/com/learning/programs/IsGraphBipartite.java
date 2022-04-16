package com.learning.programs;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
/*
* do bfs as soon as you rech the node put it in visited with color
* in case the eleemnt alreay present in visited then check its color if not same then it is not a bi-partite
* */

public class IsGraphBipartite {

    public boolean isBipartite(int[][] graph) {

        int[] visited =  new int[graph.length];
        Arrays.fill(visited,-2);

        for(int i=0;i<graph.length;i++){

            if(visited[i]!=-2) continue;

            if(this.bfs(i,visited,graph)==false){
                return false;
            }

        }
        return true;


    }


    public boolean bfs(Integer u,int[] visited,int[][] graph){

        Queue<Integer> queue = new LinkedList<>();
        queue.offer(u);
        visited[u] = 1;

        while(queue.isEmpty()==false){
            Integer node = queue.poll();

            Integer color =  (visited[node]+1)%2;


            for(Integer v: graph[node]){

                if(visited[v]!=-2){

                    if(visited[v]!=color) return false;

                }else{
                    visited[v] = color;
                    queue.offer(v);

                }

            }

        }
        return true;
    }
}

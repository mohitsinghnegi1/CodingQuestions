package com.learning.programs;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

class Edge implements Comparable<Edge>{

    public int u;
    public int v;
    public int dist;

    Edge(int u, int v, int dist){
        this.u = u;
        this.v = v;
        this.dist = dist;
    }


    public int compareTo(Edge edge){
        return this.dist - edge.dist;
    }

    public String toString(){

        System.out.println(this.dist + " "+ this.u+" "+this.v);
        return "";

    }

}




class Solution2 {
    public int minCostConnectPoints(int[][] points) {

        List<Edge> edges = new ArrayList<>();


        for(int i=0;i<points.length-1;i++){

            for(int j=i+1;j < points.length;j++){

                int dist = Math.abs(points[i][0] - points[j][0]) + Math.abs(points[i][1] - points[j][1]);

                Edge edge = new Edge(i,j,dist);
                edges.add(edge);
            }
        }


        Collections.sort(edges);


        // System.out.print(edges);

        int weight = 0;

        int[] par = new int[points.length];
        Arrays.fill(par,-1);

        for(int i=0;i<edges.size();i++){

            int parU = this.find(edges.get(i).u,par);
            int parV = this.find(edges.get(i).v,par);


            if(parU!=parV){
                par[parU] = parV;
                weight+= edges.get(i).dist;
            }

        }

        return weight;


    }

    private int find(int u,int[] par){
        while(par[u]!=-1){
            u = par[u];
        }
        return u;
    }


}
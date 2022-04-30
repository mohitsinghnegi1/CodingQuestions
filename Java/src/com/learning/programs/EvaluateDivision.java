package com.learning.programs;

import java.util.*;

class Edge1{

    String v;
    double w;

    Edge1(String v,double w){
        this.v = v;
        this.w = w;
    }

    public String toString(){
        return ""+this.v + " "+this.w;
    }

}


class Solution2 {
    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {


        // We can consider it a graph a - (w) -> b

        // Cosntruct a graph

        Map<String,List<Edge1>> graph = this.constructGraph(equations,values);

        // System.out.println(graph);
        // Process queries

        double[] ans = new double[queries.size()];
        int i = 0;

        for(List<String> query:queries){

            String u = query.get(0);
            String v = query.get(1);

            // System.out.println(""+u+" -> "+v);
            if(graph.containsKey(u)==false || graph.containsKey(v)==false){
                ans[i]= -1.0;

            }else if(u==v){
                ans[i]= 1.0;
            }else{
                ans[i] = this.bfs(graph,u,v);
            }


            i+=1;

        }

        return ans;

    }

    public double bfs(Map<String,List<Edge1>> graph,String u,String v){


        Set<String> visited = new HashSet<>();
        visited.add(u);

        Queue<Edge1> queue = new LinkedList();
        queue.offer(new Edge1(u,1));


        while(queue.isEmpty()==false){


            Edge1 node = queue.poll();
            // System.out.println(":: "+node.v);

            for(Edge1 edge : graph.get(node.v)){
                // System.out.println(".>>> "+edge.v+" "+v+edge.v ==v);
                if( edge.v.equals(v)){

                    return node.w*edge.w;
                }

                // System.out.println(""+visited.contains(edge.v)+" "+edge.v);
                if(visited.contains(edge.v)==false){
                    queue.offer(new Edge1(edge.v,node.w*edge.w));
                    visited.add(edge.v);
                }

            }

        }

        return -1.0;

    }



    public Map<String,List<Edge1>> constructGraph(List<List<String>> equations, double[] values){


        Map<String,List<Edge1>> graph = new HashMap<>();

        int i=0;
        for(List<String> edge : equations){

            String u = edge.get(0);
            String v = edge.get(1);

            if(graph.containsKey(u)==false){
                graph.put(u,new ArrayList<Edge1>());
            }

            if(graph.containsKey(v)==false){
                graph.put(v,new ArrayList<Edge1>());
            }

            graph.get(u).add(new Edge1(v,values[i]));
            graph.get(v).add(new Edge1(u,1/values[i]));

            i+=1;

        }

        return graph;
    }
}
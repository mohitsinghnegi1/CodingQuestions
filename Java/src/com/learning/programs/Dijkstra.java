package com.learning.programs;

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'shortestReach' function below.
     *
     * The function is expected to return an INTEGER_ARRAY.
     * The function accepts following parameters:
     *  1. INTEGER n
     *  2. 2D_INTEGER_ARRAY edges
     *  3. INTEGER s
     */

    public static List<Integer> shortestReach(int n, List<List<Integer>> edges, int s) {
        // Write your code here

        HashMap<List<Integer>,Integer> graph = new HashMap<>();


        for(List<Integer> edge:edges){

            Integer u = edge.get(0);
            Integer v = edge.get(1);
            Integer w = edge.get(2);

            if(graph.containsKey(Arrays.asList(u,v))){

                w = Math.min(graph.get(Arrays.asList(u,v)), w);

            }
            graph.put(Arrays.asList(u,v), w);

            if(graph.containsKey(Arrays.asList(v,u))){

                w = Math.min(graph.get(Arrays.asList(v,u)), w);

            }
            graph.put(Arrays.asList(v,u), w);
        }

        HashMap<Integer,List<List<Integer>>> graph1 = new HashMap<>();


        for(List<Integer> edge:graph.keySet()){

            Integer u = edge.get(0);
            Integer v = edge.get(1);
            Integer w = graph.get(Arrays.asList(u,v));

            if(!graph1.containsKey(u)){
                List<List<Integer>> arr = new ArrayList<>();
                graph1.put(u, arr);
            }

            graph1.get(u).add(Arrays.asList(v,w));

            if(!graph1.containsKey(v)){
                List<List<Integer>> arr = new ArrayList<>();
                graph1.put(v, arr);
            }
            graph1.get(v).add(Arrays.asList(u,w));

        }

        System.out.println(graph1);

        return findMinDist(graph1,s,n);
    }

    public static List<Integer> findMinDist(HashMap<Integer,List<List<Integer>>> graph1,Integer s, Integer n ){

        int[] dist = new int[n+1];

        Arrays.fill(dist,Integer.MAX_VALUE);

        // Use queue for dfs
        System.out.println(dist);

        Queue<List<Integer>> queue = new LinkedList<>();

        queue.offer(Arrays.asList(s,0)); // src and weignt

        while(!queue.isEmpty()){

            List<Integer> src_tw = queue.poll();
            Integer src = src_tw.get(0);
            int tw = src_tw.get(1);
            System.out.println(src_tw);
            if(dist[src] <= tw) continue;
            dist[src] = tw;

            System.out.println(dist);
            for(List<Integer> dest_w:graph1.get(src)){
                Integer dest = dest_w.get(0);
                Integer w = dest_w.get(1);

                if(dist[dest]>tw+w){
                    queue.offer(Arrays.asList(dest,tw+w));
                }
            }
        }

        ArrayList<Integer> out = new ArrayList<>();
        for(int i=1;i<dist.length;i++){

            if(i==s) continue;

            if(dist[i]!=Integer.MAX_VALUE){
                out.add(dist[i]);
            }else{
                out.add(-1);
            }


        }

        return out;

    }

}

class Dijkstra {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int t = Integer.parseInt(bufferedReader.readLine().trim());

        IntStream.range(0, t).forEach(tItr -> {
            try {
                String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

                int n = Integer.parseInt(firstMultipleInput[0]);

                int m = Integer.parseInt(firstMultipleInput[1]);

                List<List<Integer>> edges = new ArrayList<>();

                IntStream.range(0, m).forEach(i -> {
                    try {
                        edges.add(
                                Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                                        .map(Integer::parseInt)
                                        .collect(toList())
                        );
                    } catch (IOException ex) {
                        throw new RuntimeException(ex);
                    }
                });

                int s = Integer.parseInt(bufferedReader.readLine().trim());

                List<Integer> result = Result.shortestReach(n, edges, s);

                bufferedWriter.write(
                        result.stream()
                                .map(Object::toString)
                                .collect(joining(" "))
                                + "\n"
                );
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        bufferedReader.close();
        bufferedWriter.close();
    }
}

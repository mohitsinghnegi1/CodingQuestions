package com.learning.programs;

import java.util.*;

class Primes {
    public static void main(String args[] ) throws Exception {

        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        int m = s.nextInt();

        /*
            1. Create a graph in form u - > [(v,w),(v2,w2)]
            2. Create a heap and visited set/Map
            3. do bfs using heap
            4. keep track of weight
        */

        HashMap<Integer,List<List<Integer>>> graph = new HashMap<>();

        for(int i = 0;i < m;i++){
            int u = s.nextInt();
            int v = s.nextInt();
            int w = s.nextInt();

            if(graph.containsKey(u)==false){
                graph.put(u,new ArrayList());
            }

            graph.get(u).add(Arrays.asList(v,w));

            if(graph.containsKey(v)==false){
                graph.put(v,new ArrayList());
            }

            graph.get(v).add(Arrays.asList(u,w));
        }

        // System.out.println(graph);

        HashSet<Integer> visited = new HashSet<>();

        Queue<List<Integer>> pq = new PriorityQueue<>((a,b)->a.get(0)-b.get(0));
        pq.offer(Arrays.asList(0,1));

        Integer weight = 0;

        while(pq.isEmpty()==false){
            List<Integer> w_u = pq.poll();
            Integer w = w_u.get(0);
            Integer u = w_u.get(1);

            if(visited.contains(u)) continue;

            visited.add(u);
            weight += w;

            for (List<Integer> v_d : graph.get(u)){

                Integer v = v_d.get(0);
                Integer d = v_d.get(1);

                if(visited.contains(v)==false){
                    pq.offer(Arrays.asList(d,v));

                }
            }
        }

        System.out.println(weight);

    }
}

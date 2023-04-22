package com.learning;

import java.util.*;

public class RecommendationMap {


    public static void main(String[] args) {
        Map<String,String> map = new HashMap<>();
        map.put("key1","value1");
        map.put("key2","value2");
        map.put("key3","value3");
        map.put("key4","value4");

        Map<String,String> map2 = new HashMap<>();
        map.put("key1","value1");
        map.put("key2","value2");
        map.put("key3","value3");
        map.put("key4","value4");

        map.containsKey("key1"); // Set has contains method because there is only value but here we have key as well as value
        map.containsValue("value1"); // Not map does not contains null key and value
        map.entrySet();
        map.keySet();
        map.values(); // Remember its values()

        map.putAll(map2);

        // Make sure that you override hashCode and equals methods


        Set<Map.Entry<String, String>> entryset = map.entrySet();

        for(Map.Entry entry : entryset){
            System.out.println(entry.getKey());
            System.out.println(entry.getValue()); // Map has get menthod while entry has getKey() and getValue()
        }


        map.clear();

        // LinkedHashMap is ordered
        Map<Integer, List<Integer>> graph = new LinkedHashMap<>();

        graph.put(1,new ArrayList<>());
        graph.getOrDefault(1,new ArrayList<>());
        graph.get(1);
        graph.remove(1);
        graph.putIfAbsent(1,new ArrayList<>());

        // Following way can be used to initiate a graph DS
        System.out.println("graph if absent"+graph.computeIfAbsent(1,f->new ArrayList<Integer>()).add(0));
        System.out.println(graph);


        // Hashtable is threadsafe
        Map<Integer, List<Integer>> graph2 = new Hashtable<>();


        NavigableMap<Integer, String> navigableMap = new TreeMap<>(); // For SortedMap
        navigableMap.lowerEntry(2);
        navigableMap.lowerKey(2); //
        navigableMap.higherEntry(3);
        navigableMap.ceilingEntry(4);

        SortedMap<Integer,String> shortedMap = new TreeMap<>();



    }
}

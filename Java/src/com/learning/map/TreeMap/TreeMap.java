package com.learning.map.TreeMap;

import java.util.Map;

public class TreeMap {
    public static void main(String[] args) {
        // Sorted order
        // All operations will be in O(nlogn)
        Map<Integer,Integer> dict = new java.util.TreeMap<>();

        dict.put(1,1);
        dict.put(2,2);
        dict.put(100,100);
        dict.put(3,4);
        dict.put(3,3);

        dict.put(4,4);
        dict.putIfAbsent(4,5);

        System.out.println(dict);

        System.out.println(dict.containsKey(2));
        System.out.println(dict.containsValue(2));

        System.out.println(dict.size());
        System.out.println(dict.keySet());
        System.out.println(dict.values());

        // Iterate in dict
        dict.remove(2);

        for (Map.Entry<Integer,Integer> entry:dict.entrySet()) {
            System.out.print(entry.getKey()+" ");
            System.out.println(entry.getValue());
        }

        for (Integer key:dict.keySet()) {
            System.out.print(key +" ");

        }
        System.out.println()
        ;
        for (Integer val:dict.values()) {
            System.out.print(val+" ");

        }

        System.out.println();

        dict.clear();
        System.out.println(dict);
    }
}

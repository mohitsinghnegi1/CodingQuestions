package com.learning.collections.set.LinkedHashSetOperation;

import java.util.HashSet;
import java.util.LinkedHashSet;
import java.util.Set;

public class LinkedHashSetOperations {
    public static void main(String[] args) {
        // Order is maintaind in this LinkedHashSet
        Set<Integer> set= new LinkedHashSet<>();

        set.add(8);
        set.add(4);
        set.add(1);
        set.add(81);
        set.add(2);
        set.add(78);
        set.add(3);
        set.add(4); // Will be ignored
        set.add(4); // Will be ignored

        System.out.println("added elements " + set);

        set.remove(81);
        System.out.println(set);

        System.out.println(set.contains(2));

        System.out.println(set.size());
        set.clear();
        System.out.println(set);




    }
}

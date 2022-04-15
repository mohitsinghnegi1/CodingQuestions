package com.learning.collections.set.HashSetOperation;

import java.util.HashSet;
import java.util.Set;

public class HashSetOperations {
    public static void main(String[] args) {

        // Note if there is any custom class we need to add in set
        // then it will add it based on the equals and hashCode method
        // We basically need to override these methods
        // all operations will be in O(1)
        Set<Integer> set= new HashSet<>();

        set.add(8);
        set.add(1);
        set.add(81);
        set.add(2);
        set.add(78);
        set.add(3);
        set.add(4);

        System.out.println("added elements " + set);

        set.remove(81);
        System.out.println(set);

        System.out.println(set.contains(2));

        System.out.println(set.size());
        set.clear();
        System.out.println(set);




    }
}

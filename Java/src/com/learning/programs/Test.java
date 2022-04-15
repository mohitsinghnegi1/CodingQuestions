package com.learning.programs;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

public class Test {

    public static void main(String[] args) {

        HashMap<List<Integer>,Integer> hs = new HashMap<>();

        hs.put(Arrays.asList(2,2),5);
        hs.put(Arrays.asList(2,2),4);
        System.out.println(hs);
        System.out.println(hs.getOrDefault(Arrays.asList(2,2),-1));


        System.out.println("1 "+Arrays.asList(2,2).hashCode());
        System.out.println("2 "+ Arrays.asList(2,2).hashCode());

        System.out.println("3 :"+ Arrays.asList(2,2).equals(Arrays.asList(2,2)));

        System.out.println(Arrays.asList(2,2)==Arrays.asList(2,2));


    }
}

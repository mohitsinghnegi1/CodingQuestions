package com.learning.CollectionClass;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

public class CollectionClass {
    public static void main(String[] args) {
        ArrayList<Integer> arr = new ArrayList<>();
        arr.add(1);
        arr.add(23);
        arr.add(233);
        arr.add(4);
        arr.add(44);
        arr.add(2);
        arr.add(2);


        System.out.println(Collections.min(arr));
        System.out.println(Collections.max(arr));

        System.out.println(Collections.frequency(arr,2));

        Collections.sort(arr, Comparator.reverseOrder());
        System.out.println(arr);
    }

    @Override
    public String toString(){
        return  "";
    }
}

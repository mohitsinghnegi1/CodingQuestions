package com.learning.collections.list.ArrayListOperations;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;

public class ArrayListOperations {

    public static void main(String[] args){
        ArrayList<String> arrayList = new ArrayList<>(40);
        arrayList.add("Mohit");
        arrayList.add("Negi");
        System.out.println(arrayList);

        arrayList.add(1,"Singh");
        System.out.println(arrayList);

        // Add all element into array list

        arrayList.addAll(Arrays.asList(new String[]{"Welcome", "To", "Java", "World"}));

        System.out.println(arrayList);

        System.out.println(arrayList.get(0));

        // Remove element
        arrayList.remove("To");
        System.out.println(arrayList);

        System.out.println(arrayList);

        arrayList.remove(1);

        System.out.println(arrayList);

        // Contains

        System.out.println("Array list contains Java " +  arrayList.contains("Java"));

        arrayList.set(3,"Javascript");
        System.out.println(arrayList);


        // Traverse

        System.out.println("Element inside array");
        for (String val:arrayList) {

            System.out.println(val);
        }

        // using iterator
        System.out.println("Traverse Element inside array using iterator");
        Iterator<String> it = arrayList.iterator();
        while(it.hasNext()){
            System.out.println(it.next());
        }


        // Clear arraylist
        arrayList.clear();
        System.out.println(arrayList);



    }

}

package com.learning.collections.list.LinkedListOperations;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.LinkedList;

public class LinkedListOperations {

        public static void main(String[] args){
            LinkedList<String> linkedList = new LinkedList<>();
            linkedList.add("Mohit");
            linkedList.add("Negi");
            System.out.println(linkedList);

            linkedList.add(1,"Singh");
            System.out.println(linkedList);

            // Add all element into array list

            linkedList.addAll(Arrays.asList(new String[]{"Welcome", "To", "Java", "World"}));

            System.out.println(linkedList);

            System.out.println(linkedList.get(0));

            // Remove element
            linkedList.remove("To");
            System.out.println(linkedList);

            System.out.println(linkedList);

            linkedList.remove(1);

            System.out.println(linkedList);

            // Contains
            System.out.println("Array list contains Java " +  linkedList.contains("Java"));

            linkedList.set(3,"Javascript");
            System.out.println(linkedList);


            // Traverse

            System.out.println("Element inside array");
            for (String val:linkedList
            ) {

                System.out.println(val);
            }

            // using iterator
            System.out.println("Traverse Element inside array using iterator");
            Iterator<String> it = linkedList.iterator();
            while(it.hasNext()){
                System.out.println(it.next());
            }

            // Clear arraylist
            linkedList.clear();
            System.out.println(linkedList);



        }



}

package com.learning;
import com.sun.tools.javac.util.ArrayUtils;

import java.util.*;
import java.lang.*;

public class Recommendation {


    public static void main(String[] args) {

//        ArrayList<Integer> arrayList = new ArrayList<>();
//        arrayList.add(2);
//        arrayList.add(3);
//        arrayList.add(2);
//        arrayList.set(0,100);
//        arrayList.get(0);
//        arrayList.remove(0);
////        arrayList.addAll(arrayList);
//        arrayList.addAll(Arrays.asList(5,6,7,8));
//        arrayList.remove(new Integer(2));
//        arrayList.remove(2); // Can remove index as well as object
//
//        Integer frequency = Collections.frequency(arrayList,2);
//        System.out.println("frequency : "+frequency);
//
//        Collections.reverse(arrayList);
//        arrayList.indexOf(2);
//        arrayList.lastIndexOf(2);
//        arrayList.subList(1,3); // From index 1 to 3(excluded)
//
//
//        Arrays.sort(arrayList.toArray());
//        System.out.println("before sorting"+arrayList);
//
////        Collections.sort(arrayList,(x,y)->x-y);
//        Collections.sort(arrayList, Comparator.comparingInt(x -> x));
//        System.out.println(arrayList);
//
//        // It is recommended to use Deque for Queue and Stack
//
//        Deque deque = new LinkedList(); // LinkedList is a doubly linked list, which implements Deque
//
//        // Queue operations using Deque
//        deque.offerLast(2);
//        deque.peekFirst();
//        deque.pollFirst();
//
//        // Stack operations using Deque
//        deque.offerLast(3);
//        deque.pollLast();
//        deque.peekLast();
//
//        // ArrayList, Stack, Queue

        // Trick way to convert ArrayList to normal list
//        Integer arr[] = arrayList.toArray(new Integer[0]);

        ArrayList arr2 = new ArrayList();
        arr2.add(Arrays.asList(4,5,6,7,8));


//        int []arr3 = arr2.stream().mapToInt(i->i).toArray();
//        System.out.println("arr3 "+arr3);  Not working somehow




        // It is recommended to use concrete implementation of  Stack to create Stack ,

        // In Java, Stack is a class that falls under the Collection framework that extends the Vector class. It also
        // implements interfaces List, Collection, Iterable, Cloneable, Serializable. It represents the LIFO stack of objects.
        Stack<Integer> stack = new Stack<>();
        stack.push(3);
        stack.pop();
        stack.peek();

        // It is recommended to use LinkedList to implement Queue
        Queue<Integer> queue  = new LinkedList();
        queue.offer(3);
        queue.peek();
        queue.poll();

        // To Implement Deque it is recommended ArrayDequeue


        // Same operations as mentioned above
        Deque<Integer> deque = new ArrayDeque<>();

        // TO implement priority queue we use PriorityQueue itself
        // THis priority queue will follow natural ordering of Integer which already implement Comparable compareTo
        // function which return int value
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        pq.offer(2);
        pq.isEmpty();
        pq.poll();
        pq.peek();

        // Diff bet comparable vs comparator
//        Comparable<T> is implemented by the class itself (public int compareTo(T obj) ) and only require one argument because
        // it compares itself with other object
        // while Comparator<T> takes tow argument and implement public int compare(T obj1, T obj2)
        // Note we can replace comparator class with lambda function
        // Comparator override Comparable logic ie Total Ordering override Natural ordering




        // No duplicate element in set
        // No ordering

        Set<Integer> set1 = new HashSet<>();

        set1.add(1);
        set1.add(2);
        set1.contains(2);

        Set<Integer> set2 = new HashSet<>();

        set2.add(2);
        set2.add(3);
        set2.remove(2);



        set1.retainAll(set2); // Intersection
        set1.removeAll(set2); // not intersection
        set1.addAll(set2); // Union

        // We can iterate over collection

        for(Integer i : set1){
            System.out.println("set : "+i);
        }


        // In case you want to preserve the insertion Ordering then use LinkedHashSet
        Set<Integer> setWithOrdering = new LinkedHashSet<>();

        // Note: for custom class contain method won't work as expected so  we have to override public boolean equals(Object obj) and public int hashCode() // Just generate it


        SortedSet<Integer> sortedSet = new TreeSet<>((x1,x2)->x2-x1); // Will store in sorted order ,

        // Used to find the closest number , it is storted as well log(n)
        NavigableSet<Integer> navigableSet = new TreeSet<>((x1,x2)->x2-x1); // Will easy to
        navigableSet.add(4);
        navigableSet.add(3);
        navigableSet.add(1);
        navigableSet.add(6);
        navigableSet.add(7);


        navigableSet.ceiling(3); // Returns the least element in this set greater than or equal to the given element, or null if there is no such element.
        navigableSet.higher(3); // Returns the least element in this set strictly greater than the given element, or null if there is no such element.
        navigableSet.lower(3); // Returns the greatest element in this set strictly less than the given element, or null if there is no such element.










    }
}

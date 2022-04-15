package com.learning.collections.queue.PriorityQueueOperations;

import java.util.Comparator;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;

public class PriorityQueueOperations {
    public static void main(String[] args) {
        // We can also pass Comparator.reverseOrder()
        Queue<Integer> pq = new PriorityQueue<>((o1, o2) -> o2 - o1);

        // Offer and add is same but add throws exception when unable to add while offer returns false
        pq.offer(1);
        pq.offer(2);
        pq.offer(3);
        pq.add(4);

        System.out.println(pq);

        // Queue.peek is to find next inline element and returns null if next element not present
        // Queue.element is same as peek but it throws exception when element not present
        System.out.println(pq.peek());
        System.out.println(pq.element());

        // Remove (throws exception if element not present) & poll (returns null)
        System.out.println("Removing eleements from priority queue");
        System.out.println(pq.poll());
        System.out.println(pq);
        System.out.println(pq.remove());
        System.out.println(pq);
        System.out.println(pq.poll());
        System.out.println(pq.poll());

        // Actual priority queue functions



    }
}

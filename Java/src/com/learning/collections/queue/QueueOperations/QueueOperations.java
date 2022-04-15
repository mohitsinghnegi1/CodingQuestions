package com.learning.collections.queue.QueueOperations;

import java.util.LinkedList;
import java.util.Queue;

public class QueueOperations {

    public static void main(String[] args) {
        Queue<String> queue = new LinkedList<>();

        // Offer and add is same but add throws exception when unable to add while offer returns false
        queue.offer("first");
        queue.offer("second");
        queue.offer("third");
        queue.add("forth");

        System.out.println(queue);

        // Queue.peek is to find next inline element and returns null if next element not present
        // Queue.element is same as peek but it throws exception when element not present
        System.out.println(queue.peek());
        System.out.println(queue.element());

        // Remove (throws exception if element not present) & poll (returns null)
        System.out.println(queue.poll());
        System.out.println(queue);
        System.out.println(queue.remove());
        System.out.println(queue);


    }
}

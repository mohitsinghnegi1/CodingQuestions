package com.learning.collections.queue.dequeOperations;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.LinkedList;
import java.util.Queue;

public class DequeOperations {
    public static void main(String[] args) {
        ArrayDeque<Integer> dq = new ArrayDeque<>();

        // Offer and add is same but add throws exception when unable to add while offer returns false
        dq.offer(1);
        dq.offer(2);
        dq.offer(3);
        dq.add(4);

        dq.offerFirst(0);
        dq.offerFirst(-1);

        System.out.println(dq);

        // Queue.peek is to find next inline element and returns null if next element not present
        // Queue.element is same as peek but it throws exception when element not present
        System.out.println(dq.peek());
        System.out.println(dq.element());

        // Remove (throws exception if element not present) & poll (returns null)
        System.out.println(dq.poll());
        System.out.println(dq);
        System.out.println(dq.remove());
        System.out.println(dq);

        // Remove from the end
        System.out.println(dq.pollLast());
        System.out.println(dq.peekLast());


    }
}

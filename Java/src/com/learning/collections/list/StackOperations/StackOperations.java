package com.learning.collections.list.StackOperations;

import java.util.List;
import java.util.Stack;

public class StackOperations {
    public static void main(String[] args) {
        // Last In first out

        Stack<String> stack = new Stack<>();
        stack.push("Tile 3");
        stack.push("Tile 2");
        stack.push("Tile 1");
        stack.push("unknown");
        System.out.println(stack);
        System.out.println("Before removing unknown element " + stack);

        stack.removeIf(el -> el=="unknown");

        System.out.println("After removing unknown element "+stack);

        // Access top element
        System.out.println(stack.peek());
        // Pop element
        System.out.println(stack.pop());













    }
}

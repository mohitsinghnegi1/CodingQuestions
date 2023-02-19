package com.learning;

import java.util.Stack;

public class Task3 {

    public static void main(String[] args) {
        Solution sol = new Solution();

         sol.solve("<<?",0,new Stack<>());

        System.out.println("Ans : "+sol.ans);
    }


}

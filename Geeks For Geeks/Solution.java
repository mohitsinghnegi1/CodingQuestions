package com.learning;

import java.util.Stack;

public class Solution {
    public int ans;

    Solution(){
        this.ans = 0;
    }

    public void solve(String s, int i, Stack<Character> st){


        if(i==s.length()){
            System.out.println("hi"+st);

            int j=0;


            while(j<st.size()) {
                int open = 0;
                int close = 0;

                while (j<st.size() && st.get(j) == '<') {
                    open += 1;
                    j+=1;
                }

                while (j<st.size() && st.get(j) == '>') {
                    close += 1;
                    j+=1;
                }
                ans =Math.max(ans, Math.min(open, close) * 2);

                j+=1;
            }
            return;

        }

        if(s.charAt(i)=='<'){

            st.push('<');
            solve(s, i+1,st);
            st.pop();
        }else if(s.charAt(i)=='>'){
            st.push('>');
            solve(s, i+1,st);
            st.pop();
        }else{
            st.push('>');
            solve(s, i+1,st);
            st.pop();

            st.push('<');
            solve(s, i+1,st);
            st.pop();
        }


    }


}

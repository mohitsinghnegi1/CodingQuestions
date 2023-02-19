package com.learning;

import java.util.*;

public class Solution2 {


    public int solve(List<Integer> list){

        Collections.sort(list);

        if(list.size()==0){
            return 0;
        }

        if(list.size()==1) return 1;


        Integer lastNum = list.get(list.size()-1);
        Integer firstNum =  list.get(0);

        Integer total =  lastNum - firstNum;
        Integer mid = list.get(0)+total/2;
        System.out.println("mid :"+ mid );

        NavigableSet<Integer> set = new TreeSet(list);

        Integer ceil = set.ceiling(list.get(0)+total/2);
        Integer floor = set.floor(list.get(0)+total/2);

        System.out.println(set+ " ceil : "+ ceil +" floor: "+floor+" : ");
//        System.out.println("ans : "+list.get(0)+(total/2));

        if(ceil==null) return  floor - firstNum ;
        if(floor==null) return lastNum - ceil;

        if(ceil==floor){
            return Math.min( floor - firstNum, lastNum - ceil) ;
        }

        return Math.max( floor - firstNum, lastNum - ceil) ;



//        return 0;

    }

}

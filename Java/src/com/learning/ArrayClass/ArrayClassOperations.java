package com.learning.ArrayClass;

import java.util.Arrays;

public class ArrayClassOperations {
    public static void main(String[] args) {
        // Array class is used to perform operation on premitive data type
        int arr[] = new int[]{1,4,5,2,5,6,7};
        Arrays.sort(arr);
        for (int element:arr
             ) {
            System.out.print(element+" ");

        }

        System.out.println();


        System.out.println("4 found in arr ? "+ Arrays.binarySearch(arr,4));
        System.out.println("-2 found in arr ? "+ Arrays.binarySearch(arr,-2));
        System.out.println("1000 found in arr ? "+ Arrays.binarySearch(arr,1000));


        // Aready fill array
        int[] newArr = new int[10];
        Arrays.fill(newArr,24);

        for (int element:newArr
        ) {
            System.out.print(element+" ");

        }

        // Difference btw comparator vs comparable (this is unique for a class for eq COllection.sort(Student)
        // this student should impleemnt Comaparable<Student>) - we can't define more comapareTo function
        // But using comaparetor we can dynamically decide the sorting logic




    }
}

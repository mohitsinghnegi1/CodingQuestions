// Qus:https://www.hackerrank.com/challenges/java-stdin-and-stdout-1/problem

import java.util.*;


public class JavaStdinandStdoutI{
    public static void main(String ...args){
        try(Scanner sc = new Scanner(System.in)){
            while(sc.hasNext()){
                System.out.println(sc.nextInt());
            }
        }
    }
}

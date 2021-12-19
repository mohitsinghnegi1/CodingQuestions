// Qus:https://www.hackerrank.com/challenges/java-stdin-stdout/problem?h_r=next-challenge&h_v=zen


import java.util.Scanner;

public class JavaStdinAndStdoutII {
    public static void main(String[] args){
        try(Scanner sc = new Scanner(System.in)){
            
            int a = sc.nextInt();
            double b = sc.nextDouble();
            sc.nextLine();
            String c = sc.nextLine();
            
            System.out.println("String: "+c);
            System.out.println("Double: "+b);
            System.out.println("Int: "+a);
            
        }
    }
}

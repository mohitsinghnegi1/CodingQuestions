package com.learning.programs;

class uglyNumberII {
    public int nthUglyNumber(int n) {
        // following approch is correct but to find n its will take a lot of space

//         List<Boolean> dp = new ArrayList<Boolean>();
//         dp.add(true);

//         boolean isUgly = false;
//         int count = 1,i=2;
//         while(count<n ){

//             boolean two = false,three = false,five = false;

//             if(i%2==0){
//                 two = dp.get(i/2-1);
//             }
//             if(i%3==0){
//                 three = dp.get(i/3-1);
//             }
//             if(i%5==0){
//                 five = dp.get(i/5-1);
//             }

//             isUgly = two || three || five;

//             if(isUgly) count+=1;

//             dp.add(isUgly);
//             i++;

//         }


//         return dp.size();



        // Appoch 2
        /*
            Since we only need n ugly number so we need to genrate next ugly number , given 1 is already ugly number as its prime factor is limited               to 2,3,5

            1

            How to find next ugly number

            1*2
            1*3
            1*5

            what would be next ugly number? 1*2 right? yes = 2
            list 1, 2

            2*2
            1*3
            1*5
            what would be next ugly number? 1*3 right? yes = 3

            list 1, 2, 3

            2*2
            2*3
            1*5
            what would be next ugly number? 2*2 right? yes = 4

            list 1, 2, 3, 4

            3*2
            2*3
            1*5
            what would be next ugly number? 1*5 right? yes = 5

            list 1, 2, 3, 4, 5

            3*2
            2*3
            2*5
            what would be next ugly number? 3*2 and 2*3 right? yes = 6

            list 1, 2, 3, 4, 5, 6

            need to update pointer of both

            7*2
            3*3
            2*5
            what would be next ugly number? 4*2 right? yes = 8

            list 1, 2, 3, 4, 5, 6, 8

        */

        int dp1[] = new int[n];

        dp1[0] = 1;

        int p2 = 0;
        int p3 = 0;
        int p5 = 0;


        for(int i=1;i<n;i++){

            int min = Math.min(Math.min(2*dp1[p2],3*dp1[p3]),5*dp1[p5]);
            // System.out.println(2*dp1[p2]+" "+3*dp1[p3]+" "+ 5*dp1[p5]+" "+ p2+" "+ p3+" "+ p5 );
            if(min==2*dp1[p2]){
                dp1[i] = 2*dp1[p2++];
            }

            if(min==3*dp1[p3]){
                dp1[i] = 3*dp1[p3++];
            }

            if(min==5*dp1[p5]){
                dp1[i] = 5*dp1[p5++];
            }

        }
        // System.out.println(dp1[5]);
        return dp1[dp1.length-1];


    }
}


// 2, 3, 5

//     1, 2, 3, 4,5,6,8,9,10,12




//     1 = 1
//     2 = 2
//     3 = 3
//     4 = 2*dp(2)
//     5 = 5*dp(1)
//     6 = 2 * dp(3)
//     7 = 7 --NA
//     8 = 2* dp(4)
//     9 = is this  divided by 2 --no , is this divided by 3 yes = 3*3
//     10 = 2 * dp(5) yes
//     11 = NA
//     12 = 2*dp(6)     yes
//     13 = NA   current is not set hence no
//     14 = 2 * dp(7)   false








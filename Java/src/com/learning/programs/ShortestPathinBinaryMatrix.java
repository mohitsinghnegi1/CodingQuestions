package com.learning.programs;
// https://leetcode.com/problems/shortest-path-in-binary-matrix/
import java.util.LinkedList;
import java.util.Queue;

public class ShortestPathinBinaryMatrix {
    int[] r = new int[]{1,0,-1,1,-1,1,0,-1};
    int[] c = new int[]{-1,-1,-1,0,0,1,1,1};

    public int shortestPathBinaryMatrix(int[][] grid) {

        int n = grid.length;
        int m = grid[0].length;

        if(grid[0][0]==1 || grid[n-1][m-1]==1) return -1;



        return dfs(n,m,grid);


    }

    public int dfs(int n,int m,int[][] grid){


        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{0,0,1});
        grid[0][0]=1;

        while(!q.isEmpty()){

            int[] cell = q.poll();

            if(cell[0] == n-1 && cell[1] == m-1) return cell[2];

            int level = cell[2];
            // Append all adject cell which is zero and mark them 1
            for(int x=0;x<8;x++){
                int newI = cell[0]+r[x];
                int newj = cell[1]+c[x];



                if(isInside(newI,newj,n,m) && grid[newI][newj]==0){
                    grid[newI][newj] = 1;
                    q.offer(new int[]{newI,newj,level+1});
                }
            }
        }

        return -1;

    }


    public boolean isInside(int i,int j,int n,int m){

        return i>=0 && i<n && j>=0 && j<m;
    }

}

package com.learning.programs;
//https://leetcode.com/problems/count-sub-islands/
public class CountSubIslands {

    public int countSubIslands(int[][] grid1, int[][] grid2) {

        int n = grid1.length;
        int m = grid1[0].length;

        int count = 0;
        for(int i=0;i<n;i++){

            for(int j=0;j<m;j++){

                if(grid2[i][j]==1 && dfs(grid1,grid2,n,m,i,j)==true){
                    count+=1;
                }

            }

        }
        return count;
    }


    public boolean dfs(int[][] grid1, int[][] grid2,int n,int m,int i,int j){

        if(i<0 ||i>=n || j<0 || j>=m || grid2[i][j]==0)  return true;

        if(grid1[i][j] != grid2[i][j]) {
            grid2[i][j] = 0;
            dfs(grid1,grid2,n,m,i-1,j); // Necessary to mark other cells as well
            dfs(grid1,grid2,n,m,i+1,j) ;
            dfs(grid1,grid2,n,m,i,j-1) ;
            dfs(grid1,grid2,n,m,i,j+1);
            return false;
        }

        grid2[i][j] = 0;

        return dfs(grid1,grid2,n,m,i-1,j) & dfs(grid1,grid2,n,m,i+1,j) & dfs(grid1,grid2,n,m,i,j-1) & dfs(grid1,grid2,n,m,i,j+1);




    }
}

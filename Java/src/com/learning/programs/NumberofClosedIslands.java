package com.learning.programs;

public class NumberofClosedIslands {

    public int closedIsland(int[][] grid) {

        int n = grid.length;
        int m = grid[0].length;
        int count = 0;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){

                if(grid[i][j]==0 && this.dfs(grid,n,m,i,j))
                    count+= 1;
            }
        }
        return count;

    }

    public boolean dfs(int[][] grid, int n,int m,int i,int j){

        if(i<0 || i>=n || j<0 || j>=m) return false;
        if(grid[i][j]==1) return true;

        grid[i][j] = 1;

        /*
        Differnece between & and && is in && IF LEFT is false then second expression will not execute (here we want to execute other as well bec we want to make everyon one)
        therefore we used & bec we want to execute both expression

        */
        boolean ans = this.dfs(grid,n,m,i-1,j) & this.dfs(grid,n,m,i+1,j) & this.dfs(grid,n,m,i,j-1) & this.dfs(grid,n,m,i,j+1);

        return ans;

    }
}

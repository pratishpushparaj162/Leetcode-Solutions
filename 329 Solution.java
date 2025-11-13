class Solution {
    private int dfs(int i,int j,int[][] matrix,int[][] memo){
        if(memo[i][j]!=0){
            return memo[i][j];
        }
        int n  = matrix.length;
        int m  = matrix[0].length;
        int[] delr = {-1,1,0,0};
        int[] delc = {0,0,-1,1};
        int maxp = 1;
        for(int k=0;k<4;k++){
            int newr = i+delr[k];
            int newc = j+delc[k];
            if(newr<n && newr>=0 && newc<m && newc>=0 && matrix[newr][newc]>matrix[i][j]){
                maxp=Math.max(maxp,1+dfs(newr,newc,matrix,memo));
            }
        }
        memo[i][j]=maxp;
        return memo[i][j];
    }
    public int longestIncreasingPath(int[][] matrix) {
        int n  = matrix.length;
        int m  = matrix[0].length;
        int[][] memo = new int[n][m];
        int max = 0;
        for(int[] i : memo){
            Arrays.fill(i,0);
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                max = Math.max(max,dfs(i,j,matrix,memo));
            }
        }

        return max;
    }
}

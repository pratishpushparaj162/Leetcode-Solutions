class Solution {
    public int minDistance(String word1, String word2) {
        int m = word1.length();
        int n = word2.length();

        int[][] dp = new int[m+1][n+1]; // Here Dp represent number of operation required to make word1(upto length 0 <=i<= m ) to make word2 (upto length 0<=j<=n) 

        // As to make a empty string to a string with length i need i Operation
        for(int i =0;i<=n;i++){
            dp[0][i] = i;
        }

        // As to make a string with length j to a empty string need j Operation
        for(int j = 0;j<=m;j++){
            dp[j][0] = j;
        }

        for(int i = 1;i<=m;i++){
            for(int j = 1;j<=n;j++){
                if(word1.charAt(i-1) == word2.charAt(j-1)){
                    dp[i][j] = dp[i-1][j-1];
                }else{
                    int replace = dp[i-1][j-1];
                    int remove = dp[i-1][j];
                    int insert = dp[i][j-1];
                    dp[i][j] = Math.min(replace, Math.min(insert,remove)) + 1;
                }
            }
        }

        return dp[m][n];
    }
}

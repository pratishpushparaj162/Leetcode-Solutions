class Solution {
    public int change(int amount, int[] coins) {
        // APPROACH 1 : EXPLORE ALL PATHS WITH MULTIPLE PICKING
        // int n = coins.length;
        // return dfsPath (n - 1, amount, coins);

        // APPROACH 2 : MEMOIZATION
        // int n = coins.length;
        // int[][] dp = new int[n][amount + 1];
        // for (int i = 0; i < n; i++) Arrays.fill(dp[i], -1);
        // return memoization (n - 1, amount, coins, dp);

        // APPROACH 3 : TABULATION
        int n = coins.length;
        return tabulation (n, amount, coins);

        // APPROACH 4 : TABULATION (SPACE OPTIMIZATION 1 - DOUBLE ARRAY)
        // int n = coins.length;
        // return tabulationSpaceOptimization1 (n, amount, coins);
    }

    public int dfsPath (int i, int amount, int[] coins) {
        if (i == 0) {
            return amount % coins[0] == 0 ? 1 : 0;
        }

        int notTake = dfsPath (i - 1, amount, coins);
        int take = 0;
        if (coins[i] <= amount) take = dfsPath (i, amount - coins[i], coins);

        return notTake + take;
    }

    public int memoization (int i, int amount, int[] coins, int[][] dp) {
        if (i == 0) {
            return amount % coins[0] == 0 ? 1 : 0;
        }

        if (dp[i][amount] != -1) return dp[i][amount];

        int notTake = memoization (i - 1, amount, coins, dp);
        int take = 0;
        if (coins[i] <= amount) take = memoization (i, amount - coins[i], coins, dp);

        return dp[i][amount] = notTake + take;
    }

    public int tabulation (int n, int targetAmount, int[] coins) {
        int[][] dp = new int[n][targetAmount + 1];

        for (int amount = 0; amount <= targetAmount; amount++) {
            if (amount % coins[0] == 0) dp[0][amount] = 1;
            else dp[0][amount] = 0;
        }

        for (int i = 1; i < n; i++) {
            for (int amount = 0; amount <= targetAmount; amount++) {
                int notTake = dp[i - 1][amount];
                int take = 0;
                if (coins[i] <= amount) take = dp[i][amount - coins[i]];

                dp[i][amount] = notTake + take;
            }
        }

        return dp[n - 1][targetAmount];
    }

    public int tabulationSpaceOptimization1 (int n, int targetAmount, int[] coins) {
        int[] dp = new int[targetAmount + 1];

        for (int amount = 0; amount <= targetAmount; amount++) {
            if (amount % coins[0] == 0) dp[amount] = 1;
            else dp[amount] = 0;
        }

        for (int i = 1; i < n; i++) {
            int[] temp = new int[targetAmount + 1];
            for (int amount = 0; amount <= targetAmount; amount++) {
                int notTake = dp[amount];
                int take = 0;
                if (coins[i] <= amount) take = temp[amount - coins[i]];

                temp[amount] = notTake + take;
            }
            dp = temp;
        }

        return dp[targetAmount];
    }
}

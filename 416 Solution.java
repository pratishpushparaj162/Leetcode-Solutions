class Solution {
    public boolean canPartition(int[] nums) {
        int n = nums.length;
        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += nums[i];
        }

        if (sum % 2 != 0) return false;
        int target = sum / 2;

        Boolean[][] dp = new Boolean[n][target + 1];
        return helper(n - 1, nums, target, dp);
    }

    private boolean helper(int ind, int[] nums, int tar, Boolean[][] dp) {
        if (tar == 0) return true;
        if (ind == 0) return nums[0] == tar;
        if (dp[ind][tar] != null) return dp[ind][tar];

        boolean notPick = helper(ind - 1, nums, tar, dp);
        boolean pick = false;
        if (nums[ind] <= tar) {
            pick = helper(ind - 1, nums, tar - nums[ind], dp);
        }

        return dp[ind][tar] = pick || notPick;
    }
}

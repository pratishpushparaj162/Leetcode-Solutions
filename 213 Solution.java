class Solution {
    public int rob(int[] nums) {
        int n = nums.length;

        if (n == 1){
            return nums[0];
        }

        return Math.max(helper(nums, 1, n), helper(nums, 0, n - 1));
    }

    public int helper(int[] nums, int begin, int end) {
        if (end - begin == 1) {
            return nums[begin];
        }

        int prev2 = nums[end - 1];
        int prev1 = Math.max(prev2, nums[end - 2]);

        for (int i = end - 3; i >= begin; i--) {
            int current = Math.max(prev1, nums[i] + prev2);
            prev2 = prev1;
            prev1 = current;
        }

        return prev1;
    }
}

class Solution {
    public int numberOfArithmeticSlices(int[] nums) {
        int total = 0;
        int count = 0;
        for (int i = 2; i < nums.length; i++) {
            if (nums[i] - nums[i-1] == nums[i-1] - nums[i-2]) {
                count += 1;         
                total += count;     
            } else {
                count = 0;  
            }
        }
        return total;
    }
}

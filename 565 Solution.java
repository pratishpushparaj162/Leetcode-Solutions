import java.util.Arrays;

class Solution {
    public int arrayNesting(int[] nums) {
        int max = Integer.MIN_VALUE;
        boolean used[] = new boolean[nums.length];
        int i = 0;
        int ctr = 0;
        while (i < nums.length) {
            while (i < nums.length && used[i]) {
                i++;
            }
            if (i == nums.length)
                break;
            int k = i;
            ctr = 0;
            while (!used[k]) {
                used[k] = true;
                k = nums[k];
                ctr++;
            }
            max = Math.max(max, ctr);
            i++;
        }
        return max;
    }
}

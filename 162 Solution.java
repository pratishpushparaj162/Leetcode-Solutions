class Solution {
    public int findPeakElement(int[] nums) {
        int n = nums.length;
        if(n == 1) return 0;

        int left = 0;
        int right = n - 1;

        while(left <= right){
            int mid = left + (right - left) / 2;

            int leftNum = (mid - 1 < 0) ? Integer.MIN_VALUE : nums[mid - 1];
            int rightNum = (mid + 1 >= n) ? Integer.MIN_VALUE : nums[mid + 1];

            if(nums[mid] > leftNum && nums[mid] > rightNum){
                return mid;
            }

            if(leftNum > nums[mid]){
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        return -1;
    }
}

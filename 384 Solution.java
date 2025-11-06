class Solution {
    private int[] nums;
    private int n;

    public Solution(int[] nums) {
        n = nums.length;
        this.nums = nums;    
    }
    
    public int[] reset() {
        return nums;
    }
    
    public int[] shuffle() {
        if (nums.length == 1) {
            return nums;
        }
        
        List<Integer> list = new ArrayList<>();
        int[] result = new int[n];

        for (int number: nums) {
            list.add(number);
        }
        Collections.shuffle(list);
        for (int i = 0; i < n; i++) {
            result[i] = list.get(i);
        }

        return result;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int[] param_1 = obj.reset();
 * int[] param_2 = obj.shuffle();
 */

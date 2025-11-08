class Solution {
    public int[] nextGreaterElements(int[] nums) {
         int n = nums.length;

        int[] res = new int[n];

        for(int i=0;i<n;i++){
            res[i] = -1;
            for(int j=1;j<n;j++){
                int next = nums[(i+j)%n];
                if(next > nums[i]){
                    res[i] = next;
                    break;
                }
            }
        }


        System.out.println(Arrays.toString(res));
        return res;
    }
}

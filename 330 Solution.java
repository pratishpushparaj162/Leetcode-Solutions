class Solution {
    public int minPatches(int[] nums, int n) {    
        int count  = 0 ;
        long sweep = 0;
        long req = 1;
        int i = 0 ;

        while(i<nums.length && sweep < n){
            int num = nums[i];
            if(num <= req){
                sweep+=num;
                req = sweep+1;
                i++;
            }else{
                count++;
                sweep+=req;
                req = sweep+1;
            }
        }
        //if we are out of bounds and still need to sweep more range 
        if(sweep < n){
            while( sweep < n){
                long num = req;
                count++;
                sweep+=req;
                req = sweep+1;

            }   
        }

        return count;
    }

}

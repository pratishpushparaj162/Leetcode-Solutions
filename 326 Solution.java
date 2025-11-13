class Solution {
    public boolean isPowerOfThree(int n) {
        while(n>1){
            if(n%3==0){
                n=n/3;
            }else{
                return false;
            }
        }
        if(n==1){
            return true;
        }else{
            return false;
        }
    }
}

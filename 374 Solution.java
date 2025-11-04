

public class Solution extends GuessGame {
    public int guessNumber(int n) {
        int start = 1;
        int end = n;
        while(start<=end){
            int mid = start + (end - start)/2;
            int k = guess(mid);
            if(k==0){
                return mid;
            }else if(k == 1){
                start = mid + 1;
            }else{
                end = mid - 1;
            }
        }
        return -1;
    }
}

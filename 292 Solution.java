class Solution {
        public boolean canWinNim(int n) {
    	if(n <= 3) {
    		return true;
    	}
    	int limit = n % 1000;
    	boolean[] dp = new boolean[limit];
    	dp[0] = true; dp[1] = true; dp[2] = true;
    	for(int i = 3; i < limit; i++) {
    		if(dp[i - 1] == true && dp[i - 2] == true && dp[i - 3] == true) {
    			dp[i] = false;
    		} else {
    			dp[i] = true;
    		}
    	}
    	return dp[limit - 1];
    }
}

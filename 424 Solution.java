class Solution {
    public int characterReplacement(String s, int k) {
        int[] count = new int[26];
        int left = 0;
        int res = 0;
        int maxf = 0;

        for(int right = 0; right<s.length(); right++){
            char c = s.charAt(right);
            count[c - 'A']++;

            maxf = Math.max(maxf, count[c - 'A']);

            while(((right - left +1) - maxf ) > k){
                count[s.charAt(left) - 'A']--;
                left++;
            }
            res = Math.max(res, right - left + 1);
        }
        return res;
    }
}

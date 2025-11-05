class Solution {
    /**
        integer k  - each char must have freq >= k
        longest such substring 
     */
    public int longestSubstring(String s, int k) {
       return longestSubstring(s, 0, s.length(), k);
    }

    public int longestSubstring(String s, int start, int end, int k) {
        if(end-start < k) return 0;

        int [] F = new int[26];
        for(int i=start; i < end; ++i) F[s.charAt(i)-'a'] += 1;

        //find split points
        int p = start;
        while(p < end && F[s.charAt(p)-'a'] >= k) p += 1;
        if(p == end) return end-start;

        // skip contiguous bad characters
        int j = p + 1;
        while (j < end && F[s.charAt(j) - 'a'] < k) j++;

        return Math.max(longestSubstring(s, start, p, k), longestSubstring(s, j, end, k));
    }
}

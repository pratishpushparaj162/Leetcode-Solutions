class Solution {
    public String longestPalindrome(String s) {
        if(s.length() <= 1) { // "" or "a"
            return s;
        }
        // at least "ab"
        String palindrome = s.substring(0,1);
        int length = 0; // right - left
        int max = 0; // max(right - left)
        // odd palindrome; i in the midle
        int i=1;
        int left = 0;
        int right = 2;
        while(right < s.length()) {
            if(left >=0 && right < s.length() && s.charAt(left)==s.charAt(right)) {
                length = right - left;
                if(length > max) {
                    max = length;
                    palindrome = s.substring(left, right+1);
                }
                left --;
                right ++;
            } else {
                i++;
                left = i-1;
                right = i+1;
            }

        }
        // even palindrome; i in the midle-left
        i=0;
        left = 0;
        right = 1;
        while(right < s.length()) {
            if(left >=0 && right < s.length() && s.charAt(left)==s.charAt(right)) {
                length = right - left;
                if(length > max) {
                    max = length;
                    palindrome = s.substring(left, right+1);
                }
                left --;
                right ++;
            } else {
                i++;
                left = i;
                right = i+1;
            }

        }
        return palindrome;
    }
}

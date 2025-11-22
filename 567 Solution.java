class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int[][] collect = new int[2][26];

        for(char c : s1.toCharArray()){
            int idx = c - 'a';
            collect[0][idx]++;
        }

        int l = 0;
        int cnt = 0;

        for(int i = 0; i < s2.length(); i++){
            int idx = s2.charAt(i) - 'a';
            collect[1][idx]++;
            if(collect[1][idx] <= collect[0][idx]){
                cnt++;
            }
            if(i - l + 1 > s1.length()){
                int left_idx = s2.charAt(l) - 'a';
                if(collect[1][left_idx] <= collect[0][left_idx])
                    cnt--;
                collect[1][left_idx]--;
                l++;
            }
            if(cnt == s1.length()) return true;
        }

        return false;
    }
}

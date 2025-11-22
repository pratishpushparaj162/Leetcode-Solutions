import java.util.ArrayList;
import java.util.HashSet;

class Solution {
    public static Long getPalindrome(Long num) {
        String str  = Long.toString(num);
        String start = str.substring(0,str.length() - 1);
        StringBuilder sb = new StringBuilder(start);
        sb.reverse();
        String join = str + sb.toString();
        return Long.parseLong(join);

    }
    public String nearestPalindromic (String n) {
        String str = n;
        ArrayList<Long> list = new ArrayList<>();
        if(str.length() % 2 != 0) {
            String sub = str.substring(0,str.length() / 2 + 1);
            Long b = Long.parseLong(sub);
            Long c = b + 1;
            Long a = b - 1;
            list.add(getPalindrome(a));list.add(getPalindrome(b));list.add(getPalindrome(c));
        }else{
            String sub2 = str.substring(0,str.length() / 2);
            Long e = Long.parseLong(sub2);
            Long f = e + 1;
            Long d = e - 1;
            list.add(getPalindrome2(f));
            list.add(getPalindrome2(d));
            list.add(getPalindrome2(e));
        }
        int len = str.length();
        Long smaller = (long) Math.pow(10,len - 1) - 1;
        Long greater = (long) Math.pow(10,len) + 1;
        list.add(smaller);
        list.add(greater);
        Long num = Long.parseLong(str);
        Long ans = -1L;
        Long diff = Long.MAX_VALUE;
        for(Long ni : list) {
            if(ni.equals(num)) {continue;}
            long currDiff = Math.abs(ni - num);
            if(currDiff < diff || (currDiff == diff && ni < ans)) {
                diff = currDiff;
                ans = ni;
            }
        }
        return Long.toString(ans);
    }
    public static Long getPalindrome2(Long num) {
        String str = Long.toString(num);
        StringBuilder sb = new StringBuilder(str);
        sb.reverse();
        String join = str + sb.toString();
        return Long.parseLong(join);
    }
}

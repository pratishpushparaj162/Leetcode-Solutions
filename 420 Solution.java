import java.util.*;

public class Solution {
    public int strongPasswordChecker(String password) {
        int n = password.length();
        boolean hasLower = false, hasUpper = false, hasDigit = false;
        int replace = 0, oneMod = 0, twoMod = 0;

        for (int i = 0; i < n;) {
            char c = password.charAt(i);
            if (Character.isLowerCase(c)) hasLower = true;
            if (Character.isUpperCase(c)) hasUpper = true;
            if (Character.isDigit(c)) hasDigit = true;

            int j = i;
            while (i < n && password.charAt(i) == password.charAt(j)) i++;
            int len = i - j;
            if (len >= 3) {
                replace += len / 3;
                if (len % 3 == 0) oneMod++;
                else if (len % 3 == 1) twoMod++;
            }
        }

        int missingTypes = (hasLower ? 0 : 1) + (hasUpper ? 0 : 1) + (hasDigit ? 0 : 1);

        if (n < 6)
            return Math.max(missingTypes, 6 - n);

        if (n <= 20)
            return Math.max(missingTypes, replace);

        int delete = n - 20;
        replace -= Math.min(delete, oneMod);
        replace -= Math.min(Math.max(delete - oneMod, 0), twoMod * 2) / 2;
        replace -= Math.max(delete - oneMod - twoMod * 2, 0) / 3;

        return delete + Math.max(missingTypes, replace);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String password = sc.nextLine();
        System.out.println(new Solution().strongPasswordChecker(password));
    }
}

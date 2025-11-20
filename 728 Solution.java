class Solution {
    public List<Integer> selfDividingNumbers(int left, int right) {
        List<Integer> result = new ArrayList<>();

        while (left <= right) 
        {
            int num = left;
            boolean isSelfDividingNumber = true;
            while (num != 0) 
            {
                int digit = num % 10;
                num /= 10;

                if (digit == 0 || left % digit != 0) 
                {
                    isSelfDividingNumber = false;
                    break;
                }
            }
            if (isSelfDividingNumber)
                result.add(left);

            left++;
        }

        return result;
    }
}

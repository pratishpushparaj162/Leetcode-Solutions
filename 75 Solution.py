class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Two-pass counting sort approach
        """
        # First pass: Count number of 0s, 1s, and 2s
        count0 = 0
        count1 = 0
        count2 = 0
        
        for num in nums:
            if num == 0:
                count0 += 1
            elif num == 1:
                count1 += 1
            else:  # num == 2
                count2 += 1
        
        # Second pass: Overwrite array with 0s, then 1s, then 2s
        i = 0
        
        # Fill with 0s
        while count0 > 0:
            nums[i] = 0
            i += 1
            count0 -= 1
        
        # Fill with 1s
        while count1 > 0:
            nums[i] = 1
            i += 1
            count1 -= 1
        
        # Fill with 2s
        while count2 > 0:
            nums[i] = 2
            i += 1
            count2 -= 1

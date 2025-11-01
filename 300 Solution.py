class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

    # L(i) = 1 + max(L(j): where aj < ai && j < i)
        L = [0] * len(nums)
        maximum = 1
        for i in range(0, len(nums)):
            L[i] = 1
            for j in range(0, i):
                result = 1 + L[j]
                if nums[j] < nums[i] and L[i] < result:
                    L[i] = result
                    maximum = max(L[i], maximum)

        return maximum
        

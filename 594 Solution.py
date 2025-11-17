from collections import Counter
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = Counter(nums)
        largest = 0
        for n in count:
            if n+1 in count:
                largest = max(largest,count[n]+count[n+1])
        return largest

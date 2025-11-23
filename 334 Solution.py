class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        firts = second = float(inf)

        for num in nums:
            if num <= firts:
                firts = num
            elif num <= second:
                second = num
            else:
                return True
        return False

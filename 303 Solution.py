class NumArray:

    def __init__(self, nums: List[int]):
        self.pr_s=[0]*len(nums)
        self.pr_s[0]=nums[0]
        for i in range(1,len(nums)):
            self.pr_s[i]=self.pr_s[i-1]+nums[i]

    def sumRange(self, left: int, right: int)->int:
        
        if left==0:
            return self.pr_s[right]
        else:
            return self.pr_s[right]-self.pr_s[left-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

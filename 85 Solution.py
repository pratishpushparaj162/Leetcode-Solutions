class Solution:
    def largestrectarea(self, nums):
        stack = []
        left = [0]*len(nums)
        right = [0]*len(nums)

        for i in range(len(nums)):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if not stack:
                left[i] = 0
            else:
                left[i] = stack[-1] + 1
            stack.append(i)
        stack = []
        for j in range(len(nums)-1, -1, -1):
            while stack and nums[stack[-1]] >= nums[j]:
                stack.pop()
            if not stack:
                right[j] = len(nums)-1
            else:
                right[j] = stack[-1] - 1
            stack.append(j) 
        area = 0
        for i in range(len(nums)):
            area = max(area, nums[i]*(right[i] - left[i] + 1))
        return area
 
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        ans = 0
        height = [0]*len(matrix[0])
        
        for row in matrix:
            for i in range(len(matrix[0])):
                if row[i] == '1':
                    height[i] += 1
                else:
                    height[i] = 0
            ans = max(ans, self.largestrectarea(height))
        return ans

        

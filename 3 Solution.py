class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        start = 0
        maxSize = 0

        for i, c in enumerate(s):
            if c not in map or map[c] < start:
                maxSize = max(maxSize, i - start + 1)
            else:
                start = map[c] + 1
            map[c] = i

        return maxSize




        
        

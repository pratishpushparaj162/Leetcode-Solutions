from collections import defaultdict

class Solution:
    def findRotateSteps(self, ring, key):
        n = len(ring)
        char_to_indices = defaultdict(list)
        for i, ch in enumerate(ring):
            char_to_indices[ch].append(i)

        memo = {}

        def dp(pos, ki):
            if ki == len(key):
                return 0  

            if (pos, ki) in memo:
                return memo[(pos, ki)]

            res = float('inf')
            target_char = key[ki]
            
            for next_pos in char_to_indices[target_char]:
                dist = min(abs(pos - next_pos), n - abs(pos - next_pos))
                res = min(res, dist + 1 + dp(next_pos, ki + 1))

            memo[(pos, ki)] = res
            return res

        return dp(0, 0)

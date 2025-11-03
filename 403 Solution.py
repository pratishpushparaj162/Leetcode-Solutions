class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # map holds stone location: index
        m = {}

        @cache
        def solve(index, prev_jump): 
            # if we've reached the last index, return True
            if index == len(stones) - 1: 
                return True
            
            res = False
            # iterate through all possible jumps
            for next_jump in range(prev_jump - 1, prev_jump + 2): 
                # check if jump is positive and location is valid
                if next_jump > 0 and stones[index] + next_jump in m: 
                    # see if end can be reached from the new stone
                    res = res or solve(m[stones[index] + next_jump], next_jump)
            return res

        # initiate our hashmap
        for i in range(len(stones)): 
            m[stones[i]] = i
        
        # call with initial index as 0, and prev_jump as 0
        return solve(0, 0)

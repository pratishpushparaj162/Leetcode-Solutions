class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp[l][r] = min cost to guarantee win in range [l,r]
        dp = [[0] * (n+2) for _ in range(n+2)]
        
        # length of interval
        for length in range(2, n+1):  # min 2 numbers
            for l in range(1, n - length + 2):
                r = l + length - 1
                dp[l][r] = float('inf')
                for x in range(l, r+1):
                    cost = x + max(dp[l][x-1], dp[x+1][r])
                    dp[l][r] = min(dp[l][r], cost)
        
        return dp[1][n]

class Solution:
    # memoization 
    def climbStairs(self, n: int,dp=None) -> int:
        if dp is None:
            dp = {}
        if n in dp:
            return dp[n]
        if n==0 or n==1:
            return 1
        dp[n] = self.climbStairs(n-1, dp)+self.climbStairs(n-2,dp)
        return dp[n]

        
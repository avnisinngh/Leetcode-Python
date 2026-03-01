class Solution:
    # space optimization
    def climbStairs(self, n: int,dp=None) -> int:
        prev1 = 1
        prev2 = 1
        for _ in range(2, n+1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr
        return prev1

        
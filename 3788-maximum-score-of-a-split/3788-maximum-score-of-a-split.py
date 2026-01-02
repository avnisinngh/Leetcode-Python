class Solution:
    def maximumScore(self, nums: list[int]) -> int:
        total = sum(nums)
        ans = -10**18
        mini = 10**18

        for i in range(len(nums) - 1, 0, -1):
            total -= nums[i]
            mini = min(mini, nums[i])
            ans = max(ans, total - mini)

        return ans
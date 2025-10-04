class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        ans = 0
        for i in set_nums:
            if  i -1 not in set_nums:
               length = 1

               while i +length in set_nums:
                   length += 1

               ans = max(ans, length)

        return ans
             


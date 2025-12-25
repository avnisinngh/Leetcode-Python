class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = -1
        last = -1
        n = len(nums)
        for i in range(0,n):
            if(nums[i]== target):
                if first==-1:
                    first = i
                    last = i
                last = max(last,i)
        return [first, last]

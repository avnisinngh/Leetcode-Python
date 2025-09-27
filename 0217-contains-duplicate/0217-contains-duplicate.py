class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        list_set = set()
        for num in nums:
            if num in list_set:
                return True
            list_set.add(num)

        return False

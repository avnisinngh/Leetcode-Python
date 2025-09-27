class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        list_map = {}
        for num in nums:
            if num in list_map and list_map[num] >= 1:
                return True
            list_map[num] = list_map.get(num, 0)+1
        return False

        return False

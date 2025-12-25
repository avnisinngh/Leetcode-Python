class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeft():
            left, right = 0, len(nums) - 1
            pos = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    pos = mid
                    right = mid - 1   # move left
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return pos
        
        def findRight():
            left, right = 0, len(nums) - 1
            pos = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    pos = mid
                    left = mid + 1   # move right
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return pos

        return [findLeft(), findRight()]
        
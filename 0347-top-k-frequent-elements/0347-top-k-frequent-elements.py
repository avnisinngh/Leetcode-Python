class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1 

        result =[]
        for key,value in freq.items():
            result.append((value, key))  

        result.sort(reverse=True)
        return [key for value, key in result[:k]]

        
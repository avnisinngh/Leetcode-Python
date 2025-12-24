class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        m = len(capacity)
        capacity.sort(reverse=True)
        total_apple = sum(apple)
        count = 0
        cap = 0
        for i in range(0,m):
            count +=1
            cap += capacity[i]
            if(cap >= total_apple):
                break
        return count
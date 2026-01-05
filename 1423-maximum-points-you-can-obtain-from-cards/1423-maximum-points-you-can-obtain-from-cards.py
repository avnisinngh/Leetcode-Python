class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        lsum = 0
        rsum=0
        maxsum = 0
        for i in range(0,k):
            lsum = lsum + cardPoints[i]
        maxsum = lsum
        right = len(cardPoints)-1
        for i in range(k-1, -1, -1):
            lsum = lsum-cardPoints[i]
            rsum = rsum+cardPoints[right]
            right = right-1
            maxsum = max(maxsum, lsum+rsum)
        return maxsum

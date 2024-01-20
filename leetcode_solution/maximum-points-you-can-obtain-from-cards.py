class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        ans = totalval = sum(cardPoints[:k])
        for i in range (k-1, -1, -1):
            totalval += cardPoints[i + len(cardPoints) - k] - cardPoints[i]
            ans = max(ans, totalval)
        return ans




class Solution:
    def maxScore(self, s: str) -> int:
        left = 0
        right = s.count('1')
        ans = -inf
        for i in range(len(s)-1):
            if s[i] == '0':
                left += 1
            else:
                right -= 1
            ans = max(right+left,ans)
        return ans
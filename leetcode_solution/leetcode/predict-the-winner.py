from typing import List

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        return self.diff(nums, 0, n - 1, n) >= 0
    
    def diff(self, nums, left, right, n):
        if left == right:
            return nums[left]
        score_left = nums[left] - self.diff(nums, left + 1, right, n)
        score_right = nums[right] - self.diff(nums, left, right - 1, n)
        return max(score_left, score_right)
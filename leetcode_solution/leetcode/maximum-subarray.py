class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        runsum=0
        mn=0
        mx=float("-inf")

        for i in range(len(nums)):
            runsum+=nums[i]
            mx=max(mx,runsum-mn)
            mn=min(mn,runsum)
        return mx

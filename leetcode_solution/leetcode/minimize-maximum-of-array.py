class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        _sum=ans=0
        for i in range(len(nums)):
            _sum+=nums[i]
            avg=_sum/(i+1)
            if avg>ans:
                ans=avg
        return ceil(ans)
        

        
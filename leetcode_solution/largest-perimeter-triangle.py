class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        ma=0
        nums.sort()
        for i in range(len(nums)-2):
            if(nums[i]+nums[i+1]>nums[i+2] and nums[i+1]+nums[i+2]>nums[i] and nums[i+2]+nums[i]>nums[i+1] ):
                ma=max(ma,(nums[i]+nums[i+1]+nums[i+2]))
        return ma
        
        
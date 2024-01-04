class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(1,len(nums)):
            j=i
            while j>=1 and nums[j-1]>nums[j]:
                nums[j-1],nums[j]=nums[j],nums[j-1]
                j-=1
        return nums
            
        """
        Do not return anything, modify nums in-place instead.
        """
        
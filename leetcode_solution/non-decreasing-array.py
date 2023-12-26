class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        for i in range(1,len(nums)):
            if nums[i-1]>nums[i]:
                if i-1==0 or nums[i]>=nums[i-2]:
                    nums[i-1]=nums[i]
                else:
                    nums[i]=nums[i-1]
                break
            
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                return False
        return True

        
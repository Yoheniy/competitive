class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        sk,ph=0,0
        while sk<len(nums):
            if nums[sk]!=val:
                nums[sk],nums[ph]=nums[ph],nums[sk]
                ph+=1
            sk+=1
        return ph
        
        
            
            
            
        
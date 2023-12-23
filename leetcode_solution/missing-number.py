class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total=((len(nums)+1)*len(nums))//2
        res=0
        for i in nums:
            res+=i
        if(res==nums):
            return 0
        else:
            return total-res


        
            
            
        
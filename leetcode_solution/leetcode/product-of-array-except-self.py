class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=1
        cnzero=0
        
        for i in range(len(nums)):
            if nums[i]!=0:
                product*=nums[i]
            else:
                cnzero+=1
        
        for i in range(len(nums)):
            if cnzero==0:
                nums[i]=int(product/nums[i])
            elif cnzero==1 and nums[i]==0:
                nums[i]=product
            else:
                nums[i]=0
            
        return nums 
        
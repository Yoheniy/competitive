class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        l=[x for x in nums if x!=0]
        cn0=nums.count(0)
        l1=[0]*cn0
        l.extend(l1)
        print(l)
        for i in range(len(nums)):
            nums[i]=l[i]
             
        """
        Do not return anything, modify nums in-place instead.
        """
        
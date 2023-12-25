class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d=len(nums)//3
        ans=[]
        for i in range(len(nums)):
            counter=nums.count(nums[i])
            if counter>d and (not(nums[i] in ans)):
                ans.append(nums[i])
        return ans
        
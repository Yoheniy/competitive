class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        cn=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]<target:
                    cn+=1
        return cn
        
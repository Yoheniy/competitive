class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l=[i for i in range(len(nums)+1)]
        for j in nums:
            l.remove(j)
        return l[0]
            
            
        
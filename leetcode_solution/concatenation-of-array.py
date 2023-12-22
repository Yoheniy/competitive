class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l=nums
        for i in range(len(nums)):
            l.append(nums[i])
        return l
        
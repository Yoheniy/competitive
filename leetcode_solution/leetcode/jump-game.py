class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump=0
        for index,value in enumerate(nums):
            if index>max_jump:
                return False
            max_jump=max(max_jump,value+index)
        return True
        
        
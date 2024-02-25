class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack=[]
        k_val=float('-inf')
        for num in reversed(nums):
            if num<k_val:
                return True
            while stack and num>stack[-1]:
                k_val=stack[-1]
                stack.pop()
            stack.append(num)
        return False      
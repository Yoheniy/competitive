class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res=[-1]*(len(nums))
        stack=[]
        n=len(nums)
        for i in range(2*n):
            index=i%n
            while stack and nums[stack[-1]]<nums[index]:
                res[stack.pop()]=nums[index]
            if i<n:
                stack.append(index)
        return res


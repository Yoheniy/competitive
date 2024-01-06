class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=[]
        for i in range(len(nums)):
            if nums[i] not in l:
                l.append(nums[i])
        k=len(l)
        l.extend([0]*(len(nums)-len(l)))
        for i in range(len(nums)):
            nums[i]=l[i]
        return k

        
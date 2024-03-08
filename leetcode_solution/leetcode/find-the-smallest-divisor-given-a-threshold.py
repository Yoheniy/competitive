class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left,right=1,sum(nums)
        best=0
        while left<=right:
            mid=left+(right-left)//2
            counted_threshold=0
            for i in range(len(nums)):
                counted_threshold+=ceil(nums[i]/mid)
            if counted_threshold>threshold:
                left=mid+1
            else:
                best=mid
                right=mid-1
        return best
                

        
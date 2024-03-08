class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left,right=max(nums),sum(nums)
        best=0
        while left<=right:
            mid=left+(right-left)//2
            count=0
            part=1
            for i in range(len(nums)):
                count+=nums[i]
                if count>mid:
                    part+=1
                    count=nums[i]
            if part>k:
                left=mid+1
            else:
                best=mid
                right=mid-1
        return best


        
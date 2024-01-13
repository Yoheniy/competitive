class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans=float("inf")
        l,r=0,0
        numsum=0
        ch=0
        while r<len(nums):
            numsum+=nums[r]
            while numsum>=target:
                ans=min(ans,r-l+1)
                numsum-=nums[l]
                l+=1
                ch=1
            else:
                r+=1
        if ch==0:
            return 0
        return ans

        

                
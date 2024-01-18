class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left=0
        cnzero=0
        ans=0
        for right in range(len(nums)):
            if nums[right]==0:
                cnzero+=1
            while cnzero>k:
                if nums[left]==0:
                    cnzero-=1
                left+=1
            ans=max(right-left+1,ans)
        return ans
        
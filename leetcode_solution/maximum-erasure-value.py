class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        c=Counter()
        l=0
        ans=0
        for r in range(len(nums)):
            c[nums[r]]+=1
            while c[nums[r]]>1:
                c[nums[l]]-=1
                if c[nums[l]]==0:
                    del c[nums[l]]
                l+=1
            ans=max(ans,sum(c.keys()))
        return ans
        
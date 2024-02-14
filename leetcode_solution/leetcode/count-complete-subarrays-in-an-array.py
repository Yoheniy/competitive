class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        s=set(nums)
        r=l=0
        ans=0
        a=0
        m=defaultdict()
        while r<len(nums):
            if nums[r] not in m:
                m[nums[r]]=1
            else:
                m[nums[r]]+=1
            while l<len(nums) and len(s)==len(m) :
               
                ans+=len(nums)-r
                if m[nums[l]]==1:
                    del m[nums[l]]
                else:
                    m[nums[l]]-=1
                l+=1
            
            r+=1
        return ans 



        
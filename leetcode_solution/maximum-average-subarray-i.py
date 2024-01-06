class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum1=sum(nums[:k])
        l,r=0,k
        ans=sum1
        while r<len(nums):
            sum1+=nums[r]
            sum1-=nums[l]
            ans=max(ans,sum1)
            r+=1
            l+=1
        return ans/k
        
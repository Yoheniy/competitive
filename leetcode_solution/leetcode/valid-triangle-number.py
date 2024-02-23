class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        ans=0
        for right in range(n-1,1,-1):
            a=0
            b=right-1
            while a<b:
                if nums[a]+nums[b]>nums[right]:
                    ans+=b-a
                    b-=1
                else:
                    a+=1
        return ans 

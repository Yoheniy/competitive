class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans =float("-inf")
        l,r=0,len(height)-1
        while l<r:
            x=r-l
            y=min(height[r],height[l])
            ans=max(ans,x*y)
            if height[r]>=height[l]:
                l+=1
            else:
                r-=1
        return ans
        
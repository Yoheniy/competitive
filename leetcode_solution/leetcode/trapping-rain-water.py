class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        max_left=[height[0]]*n
        max_right=[height[-1]]*n
        #the maximum height to the left of each element.
        for i in range(1,n):
            max_left[i]=max(max_left[i-1],height[i])
        #the maximum height to the right of each element.
        for i in range(n-2,-1,-1):
            max_right[i]=max(max_right[i+1],height[i])
        ans=0
        # Calculate the total amount of trapped water using the height difference
        # between the minimum of max_left and max_right for each element and the height at that element.
        for i in range(n):
            ans+=min(max_left[i],max_right[i])-height[i]
        return ans 
        
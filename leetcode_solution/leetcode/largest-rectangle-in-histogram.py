class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[-1]
        ans=0
        for i in range(len(heights)):
            while len(stack)>1 and heights[i]<heights[stack[-1]]:
                temp=stack.pop()
                ans=max(ans,(i-stack[-1]-1)*heights[temp])
            stack.append(i)
        i=len(heights)
        while len(stack)>1:
                temp=stack.pop()
                ans=max(ans,(i-stack[-1]-1)*heights[temp])
        return ans

        
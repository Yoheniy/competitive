class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        ans=1
        prev_start,prev_end=points[0][0],points[0][1]
        for s,e in points:
            if s>prev_end:
                ans+=1
                prev_start,prev_end=s,e
            else:
                prev_end=min(prev_end,e)
        return ans
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort()
        l=[0]*100
        for i,j in ranges:
            for x in range(i,j+1):
                l[x]=1
        for i in range(left,right+1):
            if l[i]==0:
                return False
        return True
        
            



        
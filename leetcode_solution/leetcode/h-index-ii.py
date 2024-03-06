class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left,right,best=0,len(citations)-1,0
        while left<=right:
            mid=left+(right-left)//2
            if citations[mid]<len(citations)-mid:
                left=mid+1
            else:
                best=len(citations)-mid
                right=mid-1
        return best
        
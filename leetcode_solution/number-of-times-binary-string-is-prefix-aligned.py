class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        ans=0
        ma=0
        for i in range(len(flips)):
            ma=max(ma,flips[i])
            if ma==i+1:
                ans+=1
        return ans
        
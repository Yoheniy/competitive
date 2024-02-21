class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        s=0
        while maxDoubles>0 and target>1:
            if target%2!=0:
                s+=1
                target-=1
            else:
                target//=2
                maxDoubles-=1
                s+=1
        return s+target-1
        
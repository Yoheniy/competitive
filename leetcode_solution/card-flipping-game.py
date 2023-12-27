class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        l=set()
        for i in range(len(fronts)):
            if fronts[i]==backs[i]:
                l.add(fronts[i])
        ans=float('inf')
        for el in (fronts+backs):
            if el not in l:
                ans=min(ans,el)
        if ans !=float('inf'):
            return ans
        return 0
        
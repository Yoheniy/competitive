class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        candidates.sort()
        def solve(p,sumval,indx):
            if sumval>target:
                return
            if sumval==target and p[:] not in ans:
                ans.append(p[:])
                return
            for i in range(indx,len(candidates)):
                # Skip duplicates to avoid duplicate combinations
                if i > indx and candidates[i] == candidates[i - 1]:
                    continue
                p.append(candidates[i])
                solve(p,sumval+candidates[i],i+1)
                p.pop()
        solve([],0,0)
        return ans

        
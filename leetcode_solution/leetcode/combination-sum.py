class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        
        def solve(sumval, p, indx):
            if sumval > target:
                return
            if sumval == target:
                ans.append(p[:])
                return
            
            for i in range(indx, len(candidates)):
                p.append(candidates[i])
                solve(sumval + candidates[i], p, i)
                p.pop()
        
        solve(0, [], 0)
        return ans
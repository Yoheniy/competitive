class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans=[]
        def solve(p,sumval,indx):
            if sumval>n:
                return
            if sumval==n and len(p)==k:
                ans.append(p[:])
            for i in range(indx,10):
                p.append(i)
                solve(p,sumval+i,i+1)
                p.pop()
            return ans
        return solve([],0,1)
            
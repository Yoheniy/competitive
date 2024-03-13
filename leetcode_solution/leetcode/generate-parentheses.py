class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        def solve(open,close,curr,n):
            nonlocal ans
            if open<n:
                solve(open+1,close,curr+'(',n)
            if close<open:
                solve(open,close+1,curr+')',n)
            if len(curr)==2*n:
                ans.append(curr)
        solve(0,0,'',n)
        return ans 
              
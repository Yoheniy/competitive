class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def solve(val,m):
            if val**m==n:
                return True
            if val**m>n:
                return False
            return solve(val,m+1)
        return solve(4,0)

        
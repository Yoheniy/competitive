class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def solve(val,m):
            if val**m==n:
                return True
            if val**m>n:
                return False
            return solve(val,m+1)
        return solve(3,0)

        
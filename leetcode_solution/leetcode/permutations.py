class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def solve(p, arr):
            nonlocal ans
            if len(arr) == 0:
                ans.append(p)
                return p
            temp = [arr[0]]
            for i in range(len(p) + 1):
                first = p[0:i]
                second = p[i:len(p)]
                solve(first + temp + second, arr[1:])
            return ans
        return solve(p=[], arr=nums)
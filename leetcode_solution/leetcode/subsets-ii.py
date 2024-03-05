class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        def solve(arr,indx,p):
            temp=p[:]
            if temp not in ans:
                ans.append(p[:])
            for i in range(indx,len(nums)):
                p.append(arr[i])
                solve(arr,i+1,p)
                p.pop()
            return ans 
        return solve(nums,0,p=[])

        
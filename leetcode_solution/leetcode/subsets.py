class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def solve(arr,indx,p):
            nonlocal ans
            ans.append(p[:]) 
            for i in range(indx,len(nums)):
                p.append(arr[i])
                solve(arr,i+1,p)
                p.pop()
            return ans 
        return solve(nums,0,p=[])



        
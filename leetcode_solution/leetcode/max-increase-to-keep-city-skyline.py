class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        ans=[[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        i=0
        row={}
        col={}
        for gr in grid:
            _max=max(gr)
            row[i]=_max
            i+=1
        for i in range(len(grid[0])):
            _max=0
            for j in range(len(grid)):
                _max=max(_max,grid[j][i])
            col[i]=_max
        for key,val in row.items():
            for k,v in col.items():
                ans[key][k]=min(val,v)
        grid_sum=ans_sum=0
        for gr in grid:
            grid_sum+=sum(gr)
        for an in ans:
            ans_sum+=sum(an)
        return ans_sum-grid_sum
class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        n=len(grid[0])
        m=len(grid)
        maximam=0
        rowbegin,colbegin=0,0
        rowend,colend=2,2
        while True:
            sumc=0
            for i in range(colbegin,colend+1):
                sumc+=grid[rowbegin][i]
            
            sumc+=grid[rowbegin+1][colbegin+1]
            for i in range(colbegin,colend+1):
                sumc+=grid[rowend][i]
            maximam=max(maximam,sumc)
            if colend==n-1 and rowend==m-1:
                break
            elif colend+1<n:
                colbegin+=1
                colend+=1
            elif colend+1==n and rowend+1<m:
                colbegin,colend=0,2
                rowbegin+=1
                rowend+=1
            else:
                break
        return maximam



        
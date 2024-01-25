class NumMatrix:

    def __init__(self, mat: List[List[int]]):
        self.ps=[[0 for _ in range(len(mat[0])+1)] for i in range(len(mat)+1)]
        for i in range(1,len(mat)+1):
            for j in range(1,len(mat[0])+1):
                self.ps[i][j]=self.ps[i-1][j]+self.ps[i][j-1]-self.ps[i-1][j-1]+mat[i-1][j-1]
        print(self.ps)
        

        

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        return (self.ps[r2+1][c2+1]-self.ps[r1][c2+1]-self.ps[r2+1][c1]+self.ps[r1][c1])
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
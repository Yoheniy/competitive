class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sums=0
        n=len(mat)
        for i in range(len(mat)):
            sums+=mat[i][i]
        k=0
        for j in range(n-1,-1,-1):
            sums+=mat[j][k]
            k+=1
        if n%2==0:
            return sums
        else:
            i=n//2
            sums-=mat[i][i]
            return sums
            

        
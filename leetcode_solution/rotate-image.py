class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l=copy.deepcopy(matrix)
        k=len(matrix)-1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[j][k]=l[i][j]
            k-=1
     
        return matrix 

        """
        Do not return anything, modify matrix in-place instead.
        """
        
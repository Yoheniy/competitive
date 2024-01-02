import numpy as np
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        matrix = np.array(matrix)
        transposed_matrix = np.transpose(matrix)
        return transposed_matrix




        
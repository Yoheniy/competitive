from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = [i for i in range(1, n + 1)]

        def solve(arr, lis):
            if len(lis) == k:
                return [lis]
            
            if len(arr) == 0:
                return []  # Return an empty list when there are no more elements in the array
            
            temp = arr[0]
            left = solve(arr[1:], lis + [temp])
            right = solve(arr[1:], lis)
            
            if left is None:  # Handle the case when left is None
                return right
            elif right is None:  # Handle the case when right is None
                return left
            
            return left + right

        return solve(arr, lis=[])
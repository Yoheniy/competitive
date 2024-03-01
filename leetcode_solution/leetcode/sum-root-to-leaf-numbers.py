# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans=0
        arr=[]
        def solve(node,arr):
            nonlocal ans
            if not node:
                return
            if not node.left and not node.right:
                arr.append(str(node.val))
                ans+=int("".join(arr))
                return 
            arr.append(str(node.val))
            arr2=copy.deepcopy(arr)
            solve(node.left,arr)
            solve(node.right,arr2)
            return 

        solve(root,arr)
        return ans     
        
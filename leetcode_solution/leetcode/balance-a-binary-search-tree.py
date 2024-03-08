# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr=[]
        def helper(node):
            if not node:
                return
            arr.append(node.val)
            helper(node.left)
            helper(node.right)
        helper(root)
        arr.sort()
        def build_tree(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            left = build_tree(left, mid - 1)
            right = build_tree(mid + 1, right)
            return TreeNode(arr[mid], left, right)
        return build_tree(0, len(arr) - 1)

        
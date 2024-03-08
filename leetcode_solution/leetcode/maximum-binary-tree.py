# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def build_tree(left, right):
            if left > right:
                return None
            mid = nums.index(max(nums[left:right+1]))
            left = build_tree(left, mid - 1)
            right = build_tree(mid + 1, right)
            return TreeNode(nums[mid], left, right)
        return build_tree(0, len(nums) - 1)

        
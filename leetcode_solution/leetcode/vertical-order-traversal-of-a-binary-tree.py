# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        tuple_list=[]
        def dfs(col,row,node):
            if not node:
                return
            tuple_list.append((col,row,node.val))
            dfs(col-1,row+1,node.left)
            dfs(col+1,row+1,node.right)
            tuple_list.sort()
            print(tuple_list)
            vertical_order=[]
            curr_col=tuple_list[0][0]
            curr_vertical=[]
            for col,row,val in tuple_list:
                if curr_col==col:
                    curr_vertical.append(val)
                else:
                    vertical_order.append(curr_vertical)
                    curr_vertical=[val]
                    curr_col=col
            vertical_order.append(curr_vertical)
            return vertical_order
        return dfs(0,0,root)
        

            
        
        

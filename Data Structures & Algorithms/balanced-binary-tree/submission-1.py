# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
#         balanced=True
#         def dfs(root):
#             nonlocal balanced
#             if root==None:
#                 return 0
            
#             left_h=dfs(root.left)
#             right_h=dfs(root.right)

#             if abs(left_h-right_h)>1:
#                 balanced=False
            
#             return 1+max(left_h, right_h)
        
#         dfs(root)
#         return balanced
        # How can I structure this such that I can exit immediately after finding the first instance where balanced is false?

# This is more or less a copy of the neetcode solution
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        left_h=self.height(root.left)
        right_h=self.height(root.right)

        if abs(left_h-right_h)>1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)          
        

    def height(self, root):
        if root==None:
            return 0
        return 1+max(self.height(root.left), self.height(root.right))
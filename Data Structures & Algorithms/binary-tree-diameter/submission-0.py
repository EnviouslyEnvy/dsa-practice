# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # We can think of the greatest diameter as the node with the greatest height of the two left+right branches.
        # We can account for the answer being one less than the actual nodes in the chain by just including the root/parent.
        # Now do I remember how to find the height...

        # no, wait this assumption assumes the path cannot zig and zag.
        # 
        max_path=0
        def dfs(node):
            if node==None:
                return 0
            nonlocal max_path
            
            left_height=dfs(node.left)
            right_height=dfs(node.right)

            max_path=max(max_path,left_height+right_height)
            return 1+max(left_height, right_height)
        dfs(root)
        return max_path
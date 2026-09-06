# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Right children must be greater than their parent, and less than their parent's parent if the parent is from the right, AKA if their parent is a left child.
        # Left children must be less than their parent but greater than their parent's parent if the parent is from the left, AKA if their parent is a right child.
        # Lets have our DFS function track whether the parent is a left or right child, and do the same for the parent's parent.
        # Of course at the end the parent becomes the parent's parent for the next recursion, and the current node becomes a parent.

        # The better observation here is When we move right the lower bound is the current node's value. When we move left the upper bound is updated.
        # We'll instead pass this interval recusively.
        low=float('-inf')
        high=float('inf')
        def dfs(root, low, high):
            if root==None:
                return True
            
            # if low>=root.val or root.val>=high:
            if not low<root.val<high:
                return False
            
            return (
                dfs(root.left, low, root.val) and
                dfs(root.right, root.val, high)
            )
        return dfs(root, low, high)
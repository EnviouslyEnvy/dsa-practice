# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # The LCA in a BST must be between the two two values.
        # worst case is head is the LCA and p and q are at the bottom leaves
        
        # Edge cases null trees, null nodes.

        # If the root is greater than both p and q values, search left.
        # If root is less than both search right only.
        # If the root is between the two, both right and left must be searched.
        # If root is equal to p or q, the LCA is the root.
        
        # Handle the root/head value is equal to p or q value.
        if root.val==p.val or root.val==q.val:
            return root
        
        elif root.val>p.val and root.val>q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        elif root.val<p.val and root.val<q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        else:
            return root
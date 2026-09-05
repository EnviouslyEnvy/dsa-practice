# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # When we find the first node that matches the head of the subtree, we need to start comparing.
        # 
        if root==None and subRoot==None:
            return True
        elif root==None or subRoot==None:
            return False
        if self.sameTree(root,subRoot)==True:
            return True
        
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        return False
        
    def sameTree(self, root, subRoot):
        if root==None and subRoot==None:
            return True
        # elif root.left==None or subRoot.left==None:
        #     return False
        # if root.right==None or subRoot.right==None:
        #     return False
        elif root==None or subRoot==None:
            return False
        
        if root.val == subRoot.val:
            return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)
        
        return False

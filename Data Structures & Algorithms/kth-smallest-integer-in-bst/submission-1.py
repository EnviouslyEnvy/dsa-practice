# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter=0
        
        def dfs(node):
            nonlocal counter

            if node==None:
                return

            # check left
            result=dfs(node.left)
            if result is not None:
                return result
            
            # check middle
            counter+=1
            if counter==k:
                return node.val
            

            # check right. can return since it's the end of the function.

            return dfs(node.right)
        
        return dfs(root)



        # # Begin counter once you reach the leftmost node of the tree. 
        # # Can think of it as travel cost going backwards in the tree from a leaf (starting from the leftmost)
        # # want to count all dfs traversal starting from bottom left

        # # Actually this is overthinking... Just increment when inspecting the current node.
        # # 
        # counter=0
        # result=None
        # def dfs(node, k):
        #     nonlocal counter
        #     nonlocal result
        #     if result is not None:
        #         return result
        #     if node is None:
        #         return
            
        #     result=dfs(node.left, k)
        #     if result is not None:
        #         return result
        #     counter+=1

        #     if counter==k:
        #         result=node.val
        #         return result
            
        #     result=dfs(node.right,k)
        #     if result is not None:
        #         return result
        # dfs(root,k)
        # return result
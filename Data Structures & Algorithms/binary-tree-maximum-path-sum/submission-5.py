# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum=float('-inf')
        def dfs(node):
            nonlocal max_sum
            if node==None:
                return 0

            left_sum=max(0,dfs(node.left))
            right_sum=max(0,dfs(node.right))
            node_val=node.val
            # local_max=max(0, node_val, right_sum, left_sum, left_sum+right_sum+node_val, left_sum+node_val, right_sum+node_val)
            # if max_sum<local_max:
            #     max_sum=local_max

            # ^ This is bad

            # local_max=max(0, left_sum+right_sum+node_val)
            # max_sum=max(local_max,max_sum)
            # return local_max

            # This is also bad

            max_sum = max(max_sum, node.val + left_sum + right_sum)

            return node_val + max(left_sum, right_sum)
        dfs(root)
        return max_sum

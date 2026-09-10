# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
#         # Base cases

#         # index 1 in preorder is the root.
#         # We can use this to find the index of the root in inorder.
#         # This splits the tree into halves?
#         # Perhaps we can continue this for the left half. We know that in preorder the left node should normally immediately follow the head. If it exists to the left of the head index on the inorder we know for sure it is a left node.
#         # Do we just continue this logic?


#         # Preorder (Root → Left → Right): Process the current node before traversing its subtrees (on discovery).
#         # Inorder (Left → Root → Right): Process the current node between traversing the left and right subtrees.
#         inorder_dict={}
#         for i in range(len(inorder)):
#             inorder_dict[inorder[i]]=i
        
#         def builder(preorder, inorder, start):
#             if not preorder or not inorder:
#                 return None
            
#             root=TreeNode(preorder[0])
#             mid = inorder_dict[preorder[0]] - start

#             root.left=builder(preorder[1:mid+1], inorder[:mid], start) #we already handled index 0, the root, and python goes up to mid (including mid)
#             root.right=builder(preorder[mid+1:], inorder[mid+1:], start+mid+1)
#             return root
        
#         return builder(preorder, inorder, 0)

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_dict = {}
        for i in range(len(inorder)):
            inorder_dict[inorder[i]] = i

        def builder(pre_start, in_start, size):
            if size == 0:
                return None

            root = TreeNode(preorder[pre_start])
            mid = inorder_dict[root.val]
            left_size = mid - in_start

            root.left = builder(
                pre_start + 1,
                in_start,
                left_size
            )

            root.right = builder(
                pre_start + 1 + left_size,
                mid + 1,
                size - 1 - left_size
            )

            return root

        return builder(0, 0, len(preorder))
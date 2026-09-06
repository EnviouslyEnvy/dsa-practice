# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        # Lets think about the logic behind what is viewable from the right
        # If there is no node that is to the right of it on the *same level*, then it is viewable from the right.
        # This calls for BFS I believe.
        # We'll append each node that is the rightmost element on a level's array to a result array.

        # We should use the same queue method.
        if root is None:
            return []

        from collections import deque
        q = deque()
        q.append(root)

        result=[]

        while q:
            qLen=len(q)
            
            # again, pop the nodes, and queue the children. This time don't add to a levels queue, but simply add the value when the queue is at the last iterator value.
            # level=[]
            for i in range(qLen):
                curr=q.popleft()
                if curr:
                    # level.append(curr.val)

                    # Don't want to append null children.
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
                    if i==qLen-1:
                        result.append(curr.val)
        
        return result

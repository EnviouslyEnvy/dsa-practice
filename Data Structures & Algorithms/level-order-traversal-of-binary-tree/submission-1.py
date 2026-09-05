# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        q = collections.deque()
        q.append(root)

        while q:
            # This will track the nodes we need to go through for each level. We set the length here as we'll be adding to the queue when we visit each node in a level and add their children.
            qLen = len(q)
            
            level=[]
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            
            if level!=[]:
                result.append(level)
        
        return result

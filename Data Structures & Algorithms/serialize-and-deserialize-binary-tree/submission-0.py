# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    from collections import deque
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # Lets not really use that layer-by-layer bfs'esque format.
        # Use 'Null' for every pointer to null. Will follow dfs format. The two entries following a node will be 'null','null' if they are both null.
        # If one of them is not null, say the left one it'll be head_val, left_val, left_left_val, left_right_val, ..., 'null'
        # Actually lets make it N because i have a feeling it'll simplify better especially once we get into array indexes...
        
        # We need to worry about the case where the tree is empty... maybe?


        if root==None:
            return 'N'
        
        left_string=self.serialize(root.left)+','
        right_string=self.serialize(root.right)
        return str(root.val) + ',' + left_string + right_string

        
        
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        queue=deque(data.split(','))
        # If you do just data without .split, you'll have to configure the logic to ignore and partition by commas on your own with a while loop i presume.
        # head=TreeNode()
        def build() -> Optional[TreeNode]:
            # nonlocal queue
            # nonlocal head
            val=queue.popleft()
            if val=='N':
                return None
            
            node = TreeNode(int(val))
            node.left=build()
            node.right=build()
            return node

        return build()



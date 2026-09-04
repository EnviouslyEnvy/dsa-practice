"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodeDictionary={None:None}
        # This should map {nodes from original : nodes in new}
        # We'll do a two pass solution. The first time we simply create the new node with a matching value. And then we map the old node to the new node in the dict.
        # Then we do a second pass where we peek at each random pointer. We'll see what memory address/node it points to on the original and for the new list we'll use the dictionary to figure out what node that is among the new list's nodes.

        # We can see that we actually need the dictionary to map None to None as some random pointers will point to None. The while loop doesn't add this mapping obviously as it will stop iterating once it points to null/none.

        # First pass traversal and 'copy'
        curr=head
        # We'll need to keep track of the previous node in the copy list so that we can make the previous node point to the newest created nodes.
        prev_copy=None
        # We'll also need a head.
        head_copy=None

        while curr:
            copy_node=Node(curr.val)
            nodeDictionary[curr]=copy_node

            if prev_copy:
                prev_copy.next=copy_node
            # In case you're wondering, this conditional won't work if we simply didn't define prev_copy, even though it technically doesn't exist.
            # Intuitively/ostensible an undefined variable could be interpreted (by myself) as falsy. But it will throw an error.
            else:
                head_copy=copy_node
            
            prev_copy=copy_node
            curr=curr.next

        curr=head
        copy_node=head_copy
        while curr:
            copy_node.random=nodeDictionary[curr.random]
            curr=curr.next
            copy_node=copy_node.next
        
        return head_copy
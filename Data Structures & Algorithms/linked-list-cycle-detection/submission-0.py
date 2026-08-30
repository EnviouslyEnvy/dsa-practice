# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # I think we should keep every node in a set (hash set) of nodes called seen.
        seen=set()
        # A set would be useful here because they track unique items.
        # Even if the node has the same value, if it doesn't point to the same next node it won't be considered the same.
        # Not sure what would happen in python if they did. I don't think it looks at memory.
        while head:
            if head in seen:
                return True
            else:
                seen.add(head)
                head=head.next
        return False
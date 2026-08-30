# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        counter=0
        running_node=head
        while counter<n:
            running_node=running_node.next
            counter+=1
        if running_node is None:
            head=head.next
            return head
        
        
        
        prev=None
        curr=head
        nxt=head.next
        while running_node:
            prev=curr
            curr=curr.next
            nxt=nxt.next
            running_node=running_node.next
        
        prev.next=nxt

        return head


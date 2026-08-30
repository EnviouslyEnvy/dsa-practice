# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # It looks like i should use a two-pointers type method but for linked lists.
        # Even if i must traverse to the end first it should still be O(n)
        # Ah but wait if i traverse to the end I have no way back.
        # Do I create a reversed linked list?
        # Then keep track of the next next node, replace next with reversed, go next next on reversed, go next next on non-reversed?

        # I'm going to follow the intended method instead.

        slow=head
        fast=head.next
        while fast and fast.next:
            # Using both fast and fast.next makes sure the loop halts when it lands on the last element as well as when it goes off the edge. IE the last loop will occur at least one space away from the end.
            slow=slow.next
            fast=fast.next.next
        # begin reversal
        prev=None
        curr=slow.next
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        # remember prev ends at the head of the now reversed list.
        slow.next=None
        # Make the end of the first half zero.

        first_list_node=head
        second_list_node=prev
        while second_list_node:
            first_nxt = first_list_node.next
            second_nxt = second_list_node.next
            first_list_node.next = second_list_node
            second_list_node.next = first_nxt
            first_list_node = first_nxt
            second_list_node = second_nxt


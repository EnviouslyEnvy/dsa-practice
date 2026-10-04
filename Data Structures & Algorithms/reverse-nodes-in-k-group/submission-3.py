# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        beforeGroup = dummy
        prev = dummy
        curr = head
        while True:
            kth = self.getKthNode(beforeGroup, k)
            if not kth:
                break
            # Break group reversing procedure if there are not enough remaining nodes for a group of k
            
            # reverse
            firstInGroup = beforeGroup.next
            nextGroup = kth.next
            while curr != nextGroup:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            beforeGroup.next = prev
            beforeGroup = firstInGroup
            firstInGroup.next = curr
        return dummy.next


    def getKthNode(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

        
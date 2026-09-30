# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

# We want to look at the smallest current heads of all lists and put each one into a list.
# We can modify the first list in lists to save some space.

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(minHeap, (head.val, i, head))
        
        # We want to
        dummy = ListNode()
        tail = dummy
        while minHeap:
            details = heapq.heappop(minHeap)
            index = details[1]
            popped_node = details[2]
            lists[index] = next_node = popped_node.next
            # This makes the head of the node in the linked list move on to the next.
            if next_node:
                heapq.heappush(minHeap, (next_node.val, index, next_node))

            tail.next = popped_node
            tail = popped_node
            if not dummy.next:
                dummy.next = tail
            
            
            
        return dummy.next

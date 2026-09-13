class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # kth largest item? use a maxheap and pop k items, returning kth item.
        # Actually here's the minheap version where the top essentially becomes the kth largest due to repeatedly popping min numbers
        import heapq
        min_heap=[]
        for n in nums:
            heapq.heappush(min_heap, n)

            if len(min_heap)>k:
                heapq.heappop(min_heap)
        
        return min_heap[0]
        
# max_heap
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         import heapq

#         max_heap = [-n for n in nums]
#         heapq.heapify(max_heap)

#         for _ in range(k - 1):
#             heapq.heappop(max_heap)

#         return -max_heap[0]
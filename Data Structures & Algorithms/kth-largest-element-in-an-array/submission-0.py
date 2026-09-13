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
        

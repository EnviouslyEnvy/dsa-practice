class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq

        # need to negate the list because heapq is a minheap

        for i in range(len(stones)):
            stones[i]=-stones[i]
        
        heapq.heapify(stones)
        while len(stones)>1:
            x=-heapq.heappop(stones)
            y=-heapq.heappop(stones)
            new_stone=-(abs(x)-abs(y)) # can't be bothered to think about double negatives rn
            heapq.heappush(stones, new_stone)
        return -stones[0]
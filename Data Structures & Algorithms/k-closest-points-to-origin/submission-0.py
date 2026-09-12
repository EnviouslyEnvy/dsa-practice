class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # i'll just make tuples out of the list with their euclidean distance
        # the first index has the be the euclidean since that's what python determines sort order by.
        import heapq
        # We want a max heap and push whenever its len is >k
        # Since we keep pushing out maximums we'll end up with minimums (ie closest)
        import math
        max_heap=[]
        heapq.heapify(max_heap)
            
        for i in range(len(points)):
            x=points[i][0]
            y=points[i][1]
            heapq.heappush(max_heap,((-math.sqrt(x**2+y**2)),points[i]))
            if len(max_heap)>k:
                heapq.heappop(max_heap)
        
        res=[]
        while max_heap:
            res.append(heapq.heappop(max_heap)[1])
        
        return res
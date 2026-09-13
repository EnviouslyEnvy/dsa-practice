class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        import heapq
        from collections import Counter
        from collections import deque
        count=Counter(tasks)
        max_heap=[]
        for count_val in count.values():
            max_heap.append( - count_val)
        heapq.heapify(max_heap)

        dq=deque()
        time=0
        while max_heap or dq:
            if max_heap:
                count_val = heapq.heappop(max_heap)+1
                if count_val!=0:
                    dq.append((count_val, time + n))
            if dq and time>=dq[0][1]:
                heapq.heappush(max_heap, dq.popleft()[0])
    
            time+=1
        return time
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        left, right = newInterval
        inserted = False

        for start, end in intervals:
            if inserted or end < left:
                res.append([start, end])
            elif start > right:
                res.append([left, right])
                res.append([start, end])
                inserted = True
            else:
                left = min(left, start)
                right = max(right, end)

        if not inserted:
            res.append([left, right])

        return res
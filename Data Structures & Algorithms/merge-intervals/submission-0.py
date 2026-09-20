class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # We should probably sort the intervals.
        # From the TC we are given nlogn so it's probably sorting...
        # See if the right of an interval exceeds the next interval's left, then use the left and the max of right and next right.
        res = []
        new_interval=[]
        intervals.sort()

        for i in intervals:
            left, right = i

            if res and left<=res[-1][1]:
                res[-1][1] = max(right, res[-1][1])
                continue
            res.append(i)
        return res
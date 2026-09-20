class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # We should probably sort the intervals.
        # From the TC we are given nlogn so it's probably sorting...
        # See if the right of an interval exceeds the next interval's left, then use the left and the max of right and next right.

        # Rather than using a tracking variable like newInterval, we can just look at the most recently added interval, and pre-emptively add all intervals that have a left value that's past the end of the most recently added interval.

        # the key is thinking to use the most recently appended and modifying that.
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
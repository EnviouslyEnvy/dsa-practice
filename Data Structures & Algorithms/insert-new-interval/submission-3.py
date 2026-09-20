class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # intervals is sorted by starting (and i assuming ending secondary)?

        # Merge cases:
        # Interval can be inserted overlapping entire interval (start<start of smaller, end>end of smaller)
        # Interval can be inserted where starts within, ends outside...
        # Interval can be inserted where it starts outside, ends within (second value >= start of other)
        # Inserted interval is contained within existing interval.

        # Non-merge cases
        # We can guarantee that if the new interval's start is after an existing interval's end it will not merge.
        # We can guarantee that if the new interval's end is before an interval's start it will not merge.
        res = []
        inserted = False
        for i in intervals:
            if inserted:
                res.append(i)
                continue
            
            if i[1]<newInterval[0]:
                res.append(i)
                continue

            if i[0]>newInterval[1]:
                res.append(newInterval)
                inserted=True
                res.append(i)
                continue
            
            # Existing interval encapsulated new interval
            elif i[0] <= newInterval[0] and i[1] >= newInterval[1]:
                res.append(i)
                inserted = True

            
            # Extend the to-be left value of merged interval
            if i[0] <= newInterval[0] and i[1] < newInterval[1]:
                newInterval[0]=i[0]
            
            # Extend right value of merged interval (new right> left, new right< right)
            if i[0] <= newInterval[1] and i[1] > newInterval[1]:
                newInterval[1]=i[1]            
            

            # If the new interval's end is before the existing new inserted intervals end, ignore it as it must be absorbed.
            if i[1] <= newInterval[1]:
                continue
            
        if not inserted:
            res.append(newInterval)
        return res
        
        
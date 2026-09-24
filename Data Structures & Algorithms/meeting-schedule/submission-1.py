"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Since these are interval objects, i cant just use sort()...
        # list_intervals =[]
        # for i in intervals:
        #     list_intervals.append([i.start, i.end])
        
        # list_intervals.sort()
        
        # for i in range(1, len(list_intervals)):
        #     if list_intervals[i][0] < list_intervals[i-1][1]:
        #         return False
        
        # return True

        # Except when you can using lambda

        intervals.sort(key=lambda interval: (interval.start, interval.end))

        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i-1].end:
                return False
        return True
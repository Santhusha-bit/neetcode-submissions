"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        time = 0
        for t in sorted(intervals, key=lambda Interval: Interval.start):
            if time>t.start:
                return False
            time=t.start
            if time>t.end:
                return False
            time=t.end
        return True
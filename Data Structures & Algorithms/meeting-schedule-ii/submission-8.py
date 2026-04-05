"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) <= 1:
            return len(intervals)
        rooms = {}
        for item in intervals:
            for i in range(item.start, item.end):
                rooms[i] = rooms.get(i, 0) + 1

        value = max(rooms.values())
        return value 



        
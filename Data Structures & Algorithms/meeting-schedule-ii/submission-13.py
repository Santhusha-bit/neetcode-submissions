"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x:x.start)
        minHeap = []
        max_rooms = 0
        for i in range(len(intervals)):
            while minHeap and minHeap[0] <= intervals[i].start:
                heapq.heappop(minHeap)
            heapq.heappush(minHeap, intervals[i].end)
            max_rooms = max(max_rooms, len(minHeap))
        return max_rooms
        # start = sorted([i.start for i in intervals])
        # end = sorted([i.end for i in intervals])

        # res=0
        # count=0
        # s=0
        # e=0
        # while s < len(intervals):
        #     if start[s] < end[e]:
        #         s+=1
        #         count+=1
        #     else:
        #         e+=1
        #         count-=1
        #     res=max(res,count)
        # return res



        # if len(intervals) <= 1:
        #     return len(intervals)
        # rooms = {}
        # for item in intervals:
        #     for i in range(item.start, item.end):
        #         rooms[i] = rooms.get(i, 0) + 1

        # value = max(rooms.values())
        # return value 



        
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # res=0
        # count=defaultdict(int)
        # for interval in intervals:
        #     count[interval.start]+=1
        #     count[interval.end]-=1
        # res=0
        # cur=0
        # for time in sorted(count.keys()):
        #     cur+=count[time]
        #     res=max(res,cur)
        # return res

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



        if len(intervals) <= 1:
            return len(intervals)
        rooms = defaultdict(int)
        for item in intervals:
            for i in range(item.start, item.end):
                rooms[i] = rooms.get(i, 0) + 1

        value = max(rooms.values())
        return value 



        
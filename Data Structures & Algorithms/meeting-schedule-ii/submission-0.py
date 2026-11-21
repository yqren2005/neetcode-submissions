"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from heapq import *
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        minh = []
        intervals.sort(key=lambda i: i.start)
        for curr in intervals:
            if minh and minh[0] <= curr.start:
                heappop(minh)
            heappush(minh, curr.end)
        return len(minh)
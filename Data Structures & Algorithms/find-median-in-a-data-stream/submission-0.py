from heapq import *

class MedianFinder:

    def __init__(self):
        self.minh = []
        self.maxh = []

    def addNum(self, num: int) -> None:
        if not self.minh or num > self.minh[0]:
            heappush(self.minh, num)
        else:
            heappush(self.maxh, -num)
        # rebalance
        if len(self.minh) > len(self.maxh) + 1:
            tmp = heappop(self.minh)
            heappush(self.maxh, -tmp)
        elif len(self.maxh) > len(self.minh) + 1:
            tmp = heappop(self.maxh)
            heappush(self.minh, -tmp)

    def findMedian(self) -> float:
        if len(self.minh) == len(self.maxh):
            return (self.minh[0] - self.maxh[0]) / 2
        elif len(self.minh) > len(self.maxh):
            return self.minh[0]
        else:
            return -self.maxh[0]
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [intervals[0]]
        for start, end in intervals:
            lastend = ans[-1][1]
            if start > lastend: #no overlap
                ans.append([start, end])
            else: #touch the tail
                ans[-1][1] = max(lastend, end)
        return ans

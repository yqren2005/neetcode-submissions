class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        start, end = intervals[0]
        for s, e in intervals[1:]:
            if end < s: #no overlap
                ans.append([start, end])
                start, end = s, e
            else: #merge
                start = min(start, s)
                end = max(end, e)
        ans.append([start, end])
        return ans
        
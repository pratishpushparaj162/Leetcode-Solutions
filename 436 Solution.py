from bisect import bisect_left as bs
from operator import itemgetter

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        sorted_starts = sorted((start, i) for i, (start, _) in enumerate(intervals))
        starts_only = [s for s, _ in sorted_starts]

        result = []
        for _, end in intervals:
            idx = bisect_left(starts_only, end)
            result.append(sorted_starts[idx][1] if idx < len(intervals) else -1)
        return result
        
        

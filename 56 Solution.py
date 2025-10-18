class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        out_list = []

        # sort the intervals based on start
        intervals = sorted(intervals,key=lambda x: x[0])

        for i, ele in enumerate(intervals):
            start = ele[0]
            end = ele[1]
            if i == 0:
                last_int = ele
            
            if (start>last_int[1]) or (end<last_int[0]):
                # if no overlap, append and refresh last_int
                out_list.append(last_int)
                last_int=ele
            else:
                last_int = [min(last_int[0],start),max(last_int[1],end)]

        out_list.append(last_int)
        return out_list

class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals=sorted(intervals)
        count=0
        n=len(intervals)
        prev_start=n-1
        for i in range(n-2,-1,-1):
            if intervals[i][1]>intervals[prev_start][0]:
                count+=1
            else:
                prev_start=i
        return count
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        
        for idx in range(1, len(intervals)):
            if intervals[idx - 1][1] > intervals[idx][0]:
                return False
            
        return True
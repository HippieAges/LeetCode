class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort() # sorts in increasing order of the first index of each tuple
        
        index = 0
        interval_len = len(intervals)

        while index < interval_len:
            interval_len = len(intervals)

            if index + 1 < interval_len:
                if intervals[index][1] >= intervals[index + 1][0] and intervals[index][1] >= intervals[index + 1][1]:
                    intervals.pop(index + 1)
                elif intervals[index][1] >= intervals[index + 1][0] and intervals[index][1] < intervals[index + 1][1]:
                    intervals[index] = [intervals[index][0], intervals[index + 1][1]]
                    intervals.pop(index + 1)
                else:
                    index += 1
            else:
                index += 1
            
        return intervals
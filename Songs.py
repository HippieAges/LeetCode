from typing import List

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # time_durations = set()
        num_pairs = 0

        # for duration in time:
        #     if 60 - (duration % 60) in time_durations:
        #         num_pairs += 1
        #     time_durations = time_durations | {duration}
        # return num_pairs

        # non-optimal solution
        for index, duration in enumerate(time):
            for subsquent_durations in time[index+1:]:
                if (duration + subsquent_durations) % 60 == 0:
                    num_pairs += 1 
        return num_pairs 

s = Solution()
print(s.numPairsDivisibleBy60([30,20,150,100,40]))
print(s.numPairsDivisibleBy60([60,60,60]))
print(s.numPairsDivisibleBy60([60,60,120,60]))
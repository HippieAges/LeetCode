from typing import List
from collections import defaultdict

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        num_pairs = 0
        frequencies = defaultdict(int)

        for duration in time:
            num_pairs += frequencies[(60 - duration) % 60]
            frequencies[duration % 60] += 1

        return num_pairs 

s = Solution()
print(s.numPairsDivisibleBy60([30,20,150,100,40]))
print(s.numPairsDivisibleBy60([60,60,60]))
print(s.numPairsDivisibleBy60([60,60,120,60]))
# K Closest Points to Origin: https://leetcode.com/problems/k-closest-points-to-origin/
from math import sqrt, pow

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        def get_closest_key(point: list[int]):
            return (sqrt(pow(point[0] - 0, 2) + pow(point[1] - 0, 2))) 
        return sorted(points, key=get_closest_key)[:k]

s = Solution()
print(s.kClosest([[1,3],[-2,2]], 1))
print(s.kClosest([[3,3],[5,-1],[-2,4]], 2))
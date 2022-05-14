from __future__ import annotations
import bisect

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # brute-force solution: O(mlogn) time & O(1) space complexity
        # for m in range(len(matrix)):
        #     left, right = 0, len(matrix[m]) - 1
        #     while left <= right:
        #         mid = (left + right) // 2
        #         if target < matrix[m][mid]:
        #             right = mid - 1
        #         elif target > matrix[m][mid]:
        #             left = mid + 1
        #         else:
        #             return True
        # return False
    
        # optimized-solution: O(m) time & O(1) space complexity
        # select_row = 0
        # for m in range(len(matrix)):
        #     select_row = m
        #     if target <= matrix[m][len(matrix[m]) - 1]:
        #         break
        # # print(select_row)        
        # select_col = bisect.bisect_left(matrix[select_row], target)
        # # print(select_col)
        # return False if select_col >= len(matrix[select_row]) or matrix[select_row][select_col] != target else True 
        
        # most optimal-solution: O(lognm) time & O(1) space complexity
        # Treat the 2D Matrix as if it was one large matrix instead 
        width, height = len(matrix[0]), len(matrix)
        left, right = 0, width * height - 1
        while left <= right:
            mid = (left + right) // 2
            row = mid // width
            col = mid % width
            if target < matrix[row][col]:
                right = mid - 1
            elif target > matrix[row][col]:
                left = mid + 1
            else:
                return True
        return False
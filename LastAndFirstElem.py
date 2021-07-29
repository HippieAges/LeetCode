class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binarySearch(left : int, right : int, subarray: List[int]) -> List[int]:
            if right - left == 1 and subarray[left:right] == [target]:
                return [left]
            elif right - left == 0 or (right - left == 1 and subarray[left:right] != target):
                return []
            
            midpt = (right + left) // 2
            left_subarray = binarySearch(left, midpt, subarray)
            right_subarray = binarySearch(midpt, right, subarray)
            
            if len(left_subarray) == 1 and len(right_subarray) == 1:
                return left_subarray + right_subarray
            elif len(left_subarray) == 1 and len(right_subarray) == 2:
                return left_subarray + [right_subarray[1]]
            elif len(left_subarray) == 2 and len(right_subarray) == 1:
                return [left_subarray[0]] + right_subarray
            elif len(left_subarray) == 2 and len(right_subarray) == 2:
                return [left_subarray[0]] + [right_subarray[1]]
            return left_subarray + right_subarray
            
        result = binarySearch(0, len(nums), nums)
        return result if len(result) >= 2 else result + result if result else [-1,-1]
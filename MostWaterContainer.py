class Solution:
    def maxArea(self, height: List[int]) -> int:
        # brute-force solution - exceeds time limit
        # two nested loops, check the width and height
        # correspondence and then return the max area
        # height is obtained via min(first_elem, second_elem)
        # width is second_elem index - first_elem index 
        
#         max_area = 0
#         for first_coord_in, first_coord in enumerate(height):
#             for second_coord_in in range(first_coord_in + 1, len(height)):
#                 min_height = min(first_coord, height[second_coord_in])
#                 width = second_coord_in - first_coord_in
#                 if (area := min_height * width) > max_area:
#                     max_area = area
                
#         return max_area

        # optimal solution
        max_area = 0
        left, right = 0, len(height) - 1
        while left < right:
            width = right - left
            curr_height = min(height[left], height[right])
            
            if (new_area := width*curr_height) > max_area:
                    max_area = new_area
                    
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                    
        return max_area
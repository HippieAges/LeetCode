from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # we will need to a BFS call with all initial rotten oranges
        # as the starting vertices
        # once we infect all the adjacent vertices to that of the initial
        # rotten oranges, we can continue this process until we infect all
        # oranges within adjacent promixity
        
        grid_row_len = len(grid)
        grid_col_len = len(grid[0])
        # print(grid_row_len, grid_col_len)
        
        
        def flatten() -> List[int]:
            # flatten the list of lists
            oranges = []
            for row in range(grid_row_len):
                oranges.extend(grid[row])
            return oranges
        
        rotten_oranges = []
        row, col = 0, 0
        flattened = flatten()
        # print(flattened)
        for index, orange in enumerate(flattened):
            if orange == 2:
                rotten_oranges.append((row, col))
                
            if (index + 1) % grid_col_len == 0:
                row += 1
                col = 0
            else:
                col += 1
        
        def BFS(grid: List[List[int]], rotten_oranges: List[Tuple[int, int]]) -> int:
            queue = deque()
            queue.extend([orange for orange in rotten_oranges])
            # print(queue)
            minute = 0
            # top, left, right, bottom = False, False, False, False
            
            while queue:
                now_rotten_oranges = []

                while queue:
                    row, col = queue.popleft()
                    # print(row, col)
                    # check adjacent-top
                    if row - 1 >= 0 and grid[row - 1][col] == 1:
                        grid[row - 1][col] = 2
                        now_rotten_oranges.append((row - 1, col))
                        # print('top', grid)
                    # check adjacent-left
                    if col - 1 >= 0 and grid[row][col - 1] == 1:
                        grid[row][col - 1] = 2
                        now_rotten_oranges.append((row, col - 1))
                        # print("left", grid)
                    # check adjacent-right
                    if col + 1 < grid_col_len and grid[row][col + 1] == 1:
                        grid[row][col + 1] = 2
                        now_rotten_oranges.append((row, col + 1))
                        # print("right", grid)
                    # check adjacent-bottom
                    if row + 1 < grid_row_len and grid[row + 1][col] == 1:
                        grid[row + 1][col] = 2
                        now_rotten_oranges.append((row + 1, col))
                        # print("bottom", grid)
                        
                queue.extend(now_rotten_oranges)
                        
                # print("queue:", queue)
                if queue:
                    minute += 1
            
            return minute
        
        num_min = BFS(grid, rotten_oranges)
        
        # check for any fresh oranges
        flattened = flatten()
        fresh_oranges_left = False
        for orange in flattened:
            if orange == 1:
                fresh_oranges_left = True
                break
        
        # print(grid, flattened)
        return num_min if not fresh_oranges_left else -1
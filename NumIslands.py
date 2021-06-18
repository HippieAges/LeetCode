# two solutions to the Number of Islands problem using DFS and BFS

from typing import List, Tuple

class Solution:
    def DFS(self, grid: List[List[str]], row: int, col: int) -> None:
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row]) or grid[row][col] == '0':
            return

        grid[row][col] = '0'
        self.DFS(grid, row + 1, col) # down
        self.DFS(grid, row - 1, col) # up
        self.DFS(grid, row, col - 1) # left
        self.DFS(grid, row, col + 1) # right

    def getAdjList(self, grid: List[List[str]], row: int, col: int) -> List[Tuple]:
        adjList = []

        if col - 1 >= 0:
            adjList.append((row, col - 1))
        if col + 1 < len(grid[row]):
            adjList.append((row, col + 1))
        if row - 1 >= 0:
            adjList.append((row - 1, col))
        if row + 1 < len(grid):
            adjList.append((row + 1, col))
        return adjList

    def BFS(self, grid: List[List[str]], row: int, col: int) -> None:
        if grid[row][col] == '0':
            return
    
        grid[row][col] = '0'
        for adj_row, adj_col in self.getAdjList(grid, row, col):
            if grid[adj_row][adj_col] == '1':
                self.BFS(grid, adj_row, adj_col)
    
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0
        
        for row_index, row in enumerate(grid):
            for column_index in range(len(row)):
                if grid[row_index][column_index] == '1':
                    island_count += 1
                    # self.DFS(grid, row_index, column_index)
                    self.BFS(grid, row_index, column_index)

        return island_count

s = Solution()
print(s.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
print(s.numIslands([["1","1","1"],["0","1","0"],["1","1","1"]]))
print(s.numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))
print(s.numIslands([["1","0","1","1","1"],["1","0","1","0","1"],["1","1","1","0","1"]]))
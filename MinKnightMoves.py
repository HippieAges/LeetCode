from collections import deque
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        directions = {
            "top-left-up": (-1, -2), "top-left": (-2, -1), "top-right-up": (1, -2), "top-right": (2, -1),
            "bottom-left-down": (-1, 2), "bottom-left": (-2, 1), "bottom-right-down": (1, 2), "bottom-right": (2, 1) 
            }
        
        def BFS(coordinates: Tuple[int, int], directions: dict) -> int:
            num_steps = 0
            x, y = coordinates
            queue = deque([(0, 0)])
            visited = set()
            
            while queue:
                curr_level = len(queue)
                for i in range(curr_level):
                    front_x, front_y = queue.popleft()
                    if (front_x, front_y) == (x, y):
                        return num_steps
                    
                    for key in directions:
                        add_x, add_y = directions[key]
                        next_x, next_y = front_x + add_x, front_y + add_y
                        if (next_x, next_y) not in visited:
                            queue.append( (next_x, next_y) )
                            visited.add((next_x, next_y) )
                    
                num_steps += 1
                    
            return num_steps
        
        return BFS((x, y), directions)
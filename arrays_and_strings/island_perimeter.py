class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows , cols = len(grid) , len(grid[0])
        perimeter = 0
        for r in range(rows):
            for c in range(cols):
                directions = [(0,1), (1,0) , (-1,0), (0,-1)]
                if grid[r][c] == 1:
                    ones_count = 0
                    for dr, dc in directions:

                        if r +dr in range(rows) and c+dc in range(cols) and grid[r+dr][c+dc] == 1:
                            ones_count += 1
                    perimeter += 4- ones_count
                
        return perimeter
                        
        
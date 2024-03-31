class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        visited = set()
        islands = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):

            if (
                r not in range(rows)
                or c not in range(cols)
                or grid[r][c] == "0"
                or (r, c) in visited
            ):
                return

            visited.add((r, c))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        def bfs(r, c):

            q = deque()
            visited.add((r, c))
            q.append((r, c))
            while q:
                row, col = q.popleft()
                d = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in d:
                    r = row + dr
                    c = col + dc

                    if (
                        (r) in range(rows)
                        and (c) in range(cols)
                        and grid[r][c] == "1"
                        and (r, c) not in visited
                    ):
                        q.append((r, c))
                        visited.add((r, c))

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    islands += 1

        return islands

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def bfs(num, ocean):
            q = deque([num])

            visited = set()
            visited.add(num)
            while q:
                print(q)
                curr = q.popleft()
                r, c = curr

                directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

                for dr, dc in directions:
                    new_row = dr + r
                    new_col = dc + c
                    if (
                        new_row in range(rows)
                        and new_col in range(cols)
                        and (new_row, new_col) not in visited
                        and heights[new_row][new_col] >= heights[r][c]
                        and (
                            (new_row, new_col) not in atlantic
                            or (new_row, new_col) not in pacific
                        )
                    ):

                        if ocean == "atlantics" and (new_row, new_col) not in atlantic:
                            atlantic.add((new_row, new_col))
                        elif ocean == "pacific" and (new_row, new_col) not in pacific:
                            pacific.add((new_row, new_col))
                        visited.add((new_row, new_col))
                        q.append((new_row, new_col))

        for i in range(rows):
            for j in range(cols):

                if i == 0 or j == 0:
                    pacific.add((i, j))
                if j == cols - 1 or i == rows - 1:
                    atlantic.add((i, j))
        atlantics = [x for x in atlantic]
        pacifics = [x for x in pacific]
        print(atlantics)
        print(pacifics)
        for a in atlantics:
            bfs(a, "atlantics")

        for p in pacifics:
            bfs(p, "pacific")

        return pacific & atlantic

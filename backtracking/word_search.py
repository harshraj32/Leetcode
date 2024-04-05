class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def backtrack(r, c, curr):
            if curr == word:
                return True

            if (
                r < 0
                or r >= rows
                or c < 0
                or c >= cols
                or board[r][c] != word[len(curr)]
            ):
                return False

            temp = board[r][c]
            board[r][c] = ""  # Mark the cell as visited

            found = (
                backtrack(r + 1, c, curr + temp)
                or backtrack(r - 1, c, curr + temp)
                or backtrack(r, c + 1, curr + temp)
                or backtrack(r, c - 1, curr + temp)
            )

            board[r][c] = temp  # Restore the cell

            return found

        for i in range(rows):
            for j in range(cols):
                if backtrack(i, j, ""):
                    return True

        return False

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r, row in enumerate(board):
            for c, cell in enumerate(row):
                if cell == ".":
                    continue
                if (cell in rows[r] or cell in cols[c] or cell in squares[(r // 3, c // 3)]):
                    return False

                cols[c].add(cell)
                rows[r].add(cell)
                squares[(r // 3, c // 3)].add(cell)

        return True
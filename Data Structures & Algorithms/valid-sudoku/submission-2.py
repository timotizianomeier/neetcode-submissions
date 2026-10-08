class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Improve readability / style
        # row
        for row in range(9):
            seen = set()
            for col in range(9):
                if board[row][col] == '.':
                    continue
                if board[row][col] in seen:
                    return False
                seen.add(board[row][col])

        # col
        for col in range(9):
            seen = set()
            for row in range(9):
                if board[row][col] == '.':
                    continue
                if board[row][col] in seen:
                    return False
                seen.add(board[row][col])

        # subboard
        for square in range(9):
            seen = set()
            for r in range(3):
                for c in range(3):
                    row = square // 3 * 3 + r
                    col = square % 3 * 3 + c
                    item = board[row][col]
                    if item == '.':
                        continue
                    if item in seen:
                        return False
                    seen.add(item)

        # if none of the prior validity checks fails
        return True
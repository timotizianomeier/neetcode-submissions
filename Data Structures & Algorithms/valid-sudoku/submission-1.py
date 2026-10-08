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
        for r_scale in range(3):
            for c_scale in range(3):
                seen = set()
                for row in range(3):
                    for col in range(3):
                        item = board[row + r_scale * 3][col + c_scale * 3]
                        if item == '.':
                            continue
                        if item in seen:
                            return False
                        seen.add(item)

        # if none of the prior validity checks fails
        return True
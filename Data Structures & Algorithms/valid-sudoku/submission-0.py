class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # first naive solution
        # row
        for row in range(len(board)):
            seen = set()
            for col in range(len(board)):
                if board[row][col] != '.' and board[row][col] in seen:
                    return False
                else:
                    seen.add(board[row][col])

        # col
        for col in range(len(board)):
            seen = set()
            for row in range(len(board)):
                if board[row][col] != '.' and board[row][col] in seen:
                    return False
                else:
                    seen.add(board[row][col])

        # subboard
        for r_scale in range(3):
            for c_scale in range(3):
                seen = set()
                for row in range(3):
                    for col in range(3):
                        if board[row + r_scale * 3][col + c_scale * 3] != '.' and board[row + r_scale * 3][col + c_scale * 3] in seen:
                            return False
                        else:
                            seen.add(board[row + r_scale * 3][col + c_scale * 3])

        # if none of the prior validity checks fails
        return True
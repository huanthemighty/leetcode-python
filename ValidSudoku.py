class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # check row
        for row in range(9):
            if not self.checkPart(board, row, row + 1, 0, 9):
                return False

        # check col
        for col in range(9):
            if not self.checkPart(board, 0, 9, col, col + 1):
                return False

        # check block
        for block in range(9):
            row_start = (block / 3) * 3
            col_start = (block % 3) * 3
            if not self.checkPart(board, row_start, row_start + 3, col_start, col_start + 3):
                return False

        return True

    def checkPart(self, board, row_start, row_end, col_start, col_end):
        seen = [False] * 9
        for row in range(row_start, row_end):
            for col in range(col_start, col_end):
                c = board[row][col]
                if c == '.':
                    continue
                else:
                    i = int(c) - int('1')
                    if seen[i]:
                        return False
                    else:
                        seen[i] = True

        return True

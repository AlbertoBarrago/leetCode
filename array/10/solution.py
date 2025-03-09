class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        for i in range(len(board)):
            row = set()
            for j in range(len(board[i])):
                if board[i][j] == '.':
                    continue
                if board[i][j] in row:
                    return False
                row.add(board[i][j])

        for i in range(len(board)):
            col = set()
            for j in range(len(board[i])):
                if board[j][i] == '.':
                    continue
                if board[j][i] in col:
                    return False
                col.add(board[j][i])

        for i in range(0,len(board),3):
            for j in range(0,len(board[i]),3):
                box = set()
                for x in range(3):
                    for y in range(3):
                        if board[i+x][j+y] == '.':
                            continue
                        if board[i+x][j+y] in box:
                            return False
                        box.add(board[i+x][j+y])
        return True



board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Solution().isValidSudoku(board)

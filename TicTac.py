class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.board_size = n
        self.board = [[0 for _ in range(n)] for _ in range(n)]
        

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        
        self.board[row][col] = player
        
        p1_row, p1_col, p1_left_diag, p1_right_diag = 0, 0, 0, 0
        p2_row, p2_col, p2_left_diag, p2_right_diag = 0, 0, 0, 0
        
        for idx in range(self.board_size):
            
            reverse_idx = self.board_size - idx - 1
            
            # check row
            if self.board[row][idx] == 1:
                p1_row += 1
            elif self.board[row][idx] == 2:
                p2_row += 1
            
            # check col
            if self.board[idx][col] == 1:
                p1_col += 1
            elif self.board[idx][col] == 2:
                p2_col += 1
            
            # check left diagonal
            if row == col:
                if self.board[idx][idx] == 1:
                    p1_left_diag += 1
                elif self.board[idx][idx] == 2:
                    p2_left_diag += 1
            
            # check right diagonal
            if self.board[idx][reverse_idx] == 1:
                p1_right_diag += 1
            elif self.board[idx][reverse_idx] == 2:
                p2_right_diag += 1
            
        if p1_row == self.board_size or p1_col == self.board_size or p1_right_diag == self.board_size or p1_left_diag == self.board_size:
            return 1
        elif p2_row == self.board_size or p2_col == self.board_size or p2_right_diag == self.board_size or p2_left_diag == self.board_size:
            return 2
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
class TicTacToeEngine:
    def __init__(self):
        self.board = [None] * 9 
        self.current_player = "X"

    def make_move(self, position):
        if self.board[position] is None:
            self.board[position] = self.current_player
            if self.check_winner():
                return "WIN"
            if None not in self.board:
                return "TIE"
            self.current_player = "O" if self.current_player == "X" else "X"
            return "SUCCESS"
        return "INVALID"

    def check_winner(self):
        
        win_coords = [
            (0,1,2), (3,4,5), (6,7,8), 
            (0,3,6), (1,4,7), (2,5,8), 
            (0,4,8), (2,4,6)           
        ]
        for a, b, c in win_coords:
            if self.board[a] == self.board[b] == self.board[c] and self.board[a] is not None:
                return True
        return False
